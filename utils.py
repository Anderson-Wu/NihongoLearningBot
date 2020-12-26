import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
import pandas as pd
import numpy as np
from random import randint
from message_template import *
import psycopg2
import os
import csv
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_flex_message(reply_token, alias, flex):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, FlexSendMessage(alias, flex))


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
local = False
global DATABASE_URL


def createTable():
    global DATABASE_URL
    if local:
        DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a nihongolearning').read()[:-1]
    else:
        DATABASE_URL = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    createdb = '''CREATE TABLE IF NOT EXISTS favorite(
               userid TEXT NOT NULL,
               word_level NUMERIC NOT NULL,
               word_index NUMERIC NOT NULL
            );'''
    cursor.execute(createdb)
    conn.commit()
    cursor.close()
    conn.close()
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    createdb = '''CREATE TABLE IF NOT EXISTS user_state(
               userid TEXT NOT NULL,
               state TEXT NOT NULL
            );'''
    cursor.execute(createdb)
    conn.commit()
    cursor.close()
    conn.close()


def read_state(userid):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    query = '''SELECT * FROM user_state WHERE userid=%s '''
    cursor.execute(query, (userid,))
    result = cursor.fetchall()
    if len(result) == 0:
        query = '''INSERT INTO user_state (userid,state) VALUES (%s,%s);'''
        cursor.execute(query, (userid, 'user'))
        conn.commit()
        cursor.close()
        conn.close()
        return 'user'
    else:
        cursor.close()
        conn.close()
        return result[0][1]


def update_state(userid, state):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    query = '''UPDATE user_state SET state = %s WHERE userid = %s'''
    cursor.execute(query, (state, userid))
    conn.commit()
    cursor.close()
    conn.close()


def make_vocabulary_flex_nodb(input_level, next_state):
    if local:
        df = pd.read_csv(os.getcwd() + '/data/' + 'N' + input_level + '.csv', header=None, dtype=str)
    else:
        df = pd.read_csv('data/' + 'N' + input_level + '.csv', header=None, dtype=str)
    sample = df.sample(5)
    index = sample.index
    index = np.array(index)
    sample = np.array(sample)
    level = []
    japan = []
    spell = []
    tune = []
    chinese = []
    for voc in sample:
        level.append('N' + str(input_level))
        japan.append(voc[0])
        spell.append(voc[1])
        tune.append(voc[2])
        chinese.append(voc[3])

    flex = contentInput(level, japan, spell, tune, chinese, index, next_state)
    return flex


def add_vocabulary_to_db(event, source):
    user_id = event.source.user_id
    if source == "vocabulary":
        index_level = event.postback.data[1:]
    else:
        index_level = event.postback.data[2:]
    index_level = index_level.split('N')
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    query = '''SELECT * FROM favorite WHERE userid=%s AND  word_index=%s AND word_level=%s '''
    cursor.execute(query, (user_id, int(index_level[0]), int(index_level[1])))
    result = cursor.fetchall()
    if len(result) == 0:
        query = '''INSERT INTO favorite (userid,word_index,word_level) VALUES (%s,%s,%s);'''
        cursor.execute(query, (user_id, int(index_level[0]), int(index_level[1])))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    else:
        cursor.close()
        conn.close()
        return False


def make_vocabulary_flex_db(event, next_state):
    global DATABASE_URL
    userid = event.source.user_id
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    query = '''SELECT word_level,word_index FROM favorite WHERE userid=%s  ORDER BY RANDOM() LIMIT 5  '''
    cursor.execute(query, (userid,))
    result = cursor.fetchall()
    level = []
    japan = []
    spell = []
    tune = []
    chinese = []
    index = []
    for i, word in enumerate(result):
        lev = str(word[0])
        index.append(int(word[1]))
        if local:
            df = pd.read_csv(os.getcwd() + '/data/' + 'N' + lev + '.csv', header=None, dtype=str)
        else:
            df = pd.read_csv('data/' + 'N' + lev + '.csv', header=None, dtype=str)
        #print(df.iloc[index[i]].tolist())

        level.append('N' + lev)
        japan.append(df.iloc[index[i]].tolist()[0])
        spell.append(df.iloc[index[i]].tolist()[1])
        tune.append(df.iloc[index[i]].tolist()[2])
        chinese.append(df.iloc[index[i]].tolist()[3])

    cursor.close()
    conn.close()
    if len(result) > 0:
        flex = contentInput(level, japan, spell, tune, chinese, index, next_state,
                            num=5 if len(result) > 5 else len(result), delete=True)

    else:
        flex = no_favorite()
    return flex


def delete_vocabulary_to_db(event):
    user_id = event.source.user_id
    index_level = event.postback.data[1:]
    index_level = index_level.split('N')
    #print(index_level)
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    query = '''SELECT * FROM favorite WHERE userid=%s AND  word_index=%s AND word_level=%s '''
    cursor.execute(query, (user_id, int(index_level[0]), int(index_level[1])))
    result = cursor.fetchall()
    if len(result) == 0:
        return False
        cursor.close()
        conn.close()
    else:
        query = '''DELETE  FROM favorite WHERE userid=%s AND  word_index=%s AND word_level=%s '''
        cursor.execute(query, (user_id, int(index_level[0]), int(index_level[1])))
        conn.commit()
        cursor.close()
        conn.close()
        return True


# def export_favorite(event):
#     table=[['級數','日文','假名','重音','中文']]
#     id = event.source.user_id
#     conn = psycopg2.connect(DATABASE_URL, sslmode='require')
#     cursor = conn.cursor()
#     query = '''SELECT word_level,word_index FROM favorite WHERE userid=%s '''
#     cursor.execute(query, (id,))
#     result = cursor.fetchall()
#     index = []
#     for i,word in enumerate(result):
#         lev = 'N'+str(word[0])
#         if local:
#             df = pd.read_csv(os.getcwd() + '/data/' + lev + '.csv',header=None, dtype=str)
#         else:
#             df = pd.read_csv('data/' + lev + '.csv', header=None, dtype=str)
#         temp = df.iloc[int(word[1])].tolist()
#         temp.insert(0,lev)
#         table.append(temp)
#
#
#     # --- Email 的收件人與寄件人address ---
#     emailfrom = account
#     emailto = event.message.text
#     # # --- Email 附件檔案 Attachment -----------
#     if local:
#         with open(os.getcwd() +event.source.user_id+'.csv','w',newline='',encoding="utf-8") as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerows(table)
#         fileToSend = os.getcwd() +event.source.user_id+'.csv'
#     else:
#         with open('data/'+event.source.user_id+'.csv', 'w', newline='') as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerows(table)
#         fileToSend = 'data/'+event.source.user_id+'.csv'
#
#
#     msg = MIMEMultipart()
#     msg["From"] = emailfrom
#     msg["To"] = emailto
#     # --- Email 的主旨 Subject ---
#     msg["Subject"] = "收藏單字"
#     msg["preamble"] = 'You will not see this in a MIME-aware mail reader.\n'
#
#     # ----- Email 的信件內容 Message -----
#     part = MIMEText("以下為您的收藏單字", _charset="UTF-8")
#
#     msg.attach(part)
#     # ----- Test for Text Message -----
#
#     ctype, encoding = mimetypes.guess_type(fileToSend)
#     if ctype is None or encoding is not None:
#         ctype = "application/octet-stream"
#     maintype, subtype = ctype.split("/", 1)
#     print(maintype,subtype)
#
#     fp = open(fileToSend, "rb")
#     attachment = MIMEBase(maintype, subtype)
#     attachment.set_payload(fp.read())
#     fp.close()
#     encoders.encode_base64(attachment)
#     attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
#     msg.attach(attachment)
#
#     # --- 如果是 Gmail 可使用這行 ---
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     # --- 如果SMTP server 不需要登入則可把 server.login 用 # mark 掉
#     server.login(username, password)
#     server.sendmail(emailfrom, emailto, msg.as_string())
#     server.quit()


def generate_question(event):
    # print(event)
    parsed_input = event.postback.data.split('N')
    if 'next' in parsed_input[0]:
        parsed_input[0] = parsed_input[0][4:]
    if local:
        df = pd.read_csv(os.getcwd() + '/data/' + 'N' + parsed_input[1] + '.csv', header=None, dtype=str)
    else:
        df = pd.read_csv('data/' + 'N' + parsed_input[1] + '.csv', header=None, dtype=str)

    while True:
        sample = df.sample(2)
        index = sample.index
        index = np.array(index)
        sample = np.array(sample)
        level = []
        japan = []
        spell = []
        tune = []
        chinese = []
        for voc in sample:
            level.append('N' + str(parsed_input[1]))
            japan.append(voc[0])
            spell.append(voc[1])
            tune.append(voc[2])
            chinese.append(voc[3])
        if index[0] == index[1]:
            continue
        if '------' in spell[0] or '------' in spell[1]:
            if parsed_input[0] == "spell":
                continue
        if '------' in spell[0] or '------' in spell[1]:
            if parsed_input[0] == "chinese":
                if '------' in spell[0]:
                    spell[0] = japan[0]
                if '------' in spell[1]:
                    spell[1] = japan[1]
            break
        break
    rand_num = randint(0, 1)
    if parsed_input[0] == "spell":
        if rand_num == 0:
            spell_option = [spell[0], spell[1]]
            answer = ['r', 'w']
        else:
            spell_option = [spell[1], spell[0]]
            answer = ['w', 'r']
        #print(spell_option)
        flex = test_spell_option(level[rand_num], japan[rand_num], spell_option, tune[rand_num], chinese[rand_num],
                                 index[rand_num], answer)
    else:
        if rand_num == 0:
            chinese_option = [chinese[0], chinese[1]]
            answer = ['r', 'w']
        else:
            chinese_option = [chinese[1], chinese[0]]
            answer = ['w', 'r']
        flex = test_chinese_option(level[rand_num], japan[rand_num], spell[rand_num], tune[rand_num], chinese_option,
                                   index[rand_num], answer)
    return flex


def generate_answer(event):
    question_type = event.postback.data[0]
    index_level = event.postback.data[10:].split('N')
    #print(index_level)

    lev = str(index_level[1])
    index = int(index_level[0])
    if local:
        df = pd.read_csv(os.getcwd() + '/data/' + 'N' + lev + '.csv', header=None, dtype=str)
    else:
        df = pd.read_csv('data/' + 'N' + lev + '.csv', header=None, dtype=str)
    #print(df.iloc[index].tolist())

    level = 'N' + lev
    spell = df.iloc[index].tolist()[1]
    chinese = df.iloc[index].tolist()[3]
    if question_type == 's':
        flex = test_spell_answer_result(level, index, spell)
    else:
        flex = test_chinese_answer_result(level, index, chinese)
    return flex
