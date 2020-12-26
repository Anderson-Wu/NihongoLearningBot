from transitions.extensions import GraphMachine
from linebot.models import PostbackEvent
from utils import *


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_vocabulary(self, event):
        if isinstance(event, MessageEvent):
            return event.message.text.lower() == "start"
        elif isinstance(event, PostbackEvent):
            if event.postback.data.lower() == "return_main":
                return True
            else:
                return False
        return False

    def on_enter_vocabulary(self, event):
        #print("I'm entering vocabulary")
        reply_token = event.reply_token
        flex = main_menu()
        send_flex_message(reply_token, "主選單", flex)

    def is_going_to_vocabulary_n2(self, event):
        if not isinstance(event, PostbackEvent):
            if isinstance(event, str) and event == "return_from_add_favorite_n2":
                return True
        else:
            if event.postback.data.lower() == "n2" or event.postback.data.lower() == "return_main":
                return True
        return False

    def on_enter_vocabulary_n2(self, event):
        #print("I'm entering vocabulary_n2")
        if isinstance(event, str) and event == "return_from_add_favorite_n2":
            pass
        else:
            if event.postback.data.lower() == "return_main":
                self.go_back_vocabulary(event)
            else:
                reply_token = event.reply_token
                flex = make_vocabulary_flex_nodb("2", "n2")
                send_flex_message(reply_token, "n2", flex)

    def is_going_to_vocabulary_n3(self, event):
        if not isinstance(event, PostbackEvent):
            if isinstance(event, str) and event == "return_from_add_favorite_n3":
                return True
        else:
            if event.postback.data.lower() == "n3" or event.postback.data.lower() == "return_main":
                return True
        return False

    def on_enter_vocabulary_n3(self, event):
        #print("I'm entering vocabulary_n3")
        if isinstance(event, str) and event == "return_from_add_favorite_n3":
            pass
        else:
            if event.postback.data.lower() == "return_main":
                self.go_back_vocabulary(event)
            else:
                reply_token = event.reply_token
                flex = make_vocabulary_flex_nodb("3", "n3")
                send_flex_message(reply_token, "n3", flex)

    def is_going_to_vocabulary_n4(self, event):
        if not isinstance(event, PostbackEvent):
            if isinstance(event, str) and event == "return_from_add_favorite_n4":
                return True
        else:
            if event.postback.data.lower() == "n4" or event.postback.data.lower() == "return_main":
                return True
        return False

    def on_enter_vocabulary_n4(self, event):
        #print("I'm entering vocabulary_n4")
        if isinstance(event, str) and event == "return_from_add_favorite_n4":
            pass
        else:
            if event.postback.data.lower() == "return_main":
                self.go_back_vocabulary(event)
            else:
                reply_token = event.reply_token
                flex = make_vocabulary_flex_nodb("4", "n4")
                send_flex_message(reply_token, "n4", flex)

    def is_going_to_vocabulary_n5(self, event):
        if not isinstance(event, PostbackEvent):
            if isinstance(event, str) and event == "return_from_add_favorite_n5":
                return True
        else:
            if event.postback.data.lower() == "n5" or event.postback.data.lower() == "return_main":
                return True
        return False

    def on_enter_vocabulary_n5(self, event):
        #print("I'm entering vocabulary_n5")
        if isinstance(event, str) and event == "return_from_add_favorite_n5":
            pass
        else:
            if event.postback.data.lower() == "return_main":
                self.go_back_vocabulary(event)
            else:
                reply_token = event.reply_token
                flex = make_vocabulary_flex_nodb("5", "n5")
                send_flex_message(reply_token, "n5", flex)

    def is_going_to_vocabulary_favorite(self, event):
        if not isinstance(event, PostbackEvent):
            return False
        else:
            return event.postback.data.lower() == "favorite" or event.postback.data.lower() == "return_from_add_favorite_delete" or event.postback.data.lower() == "return_main"

    def on_enter_vocabulary_favorite(self, event):
        #print("I'm entering vocabulary_favorite")
        if isinstance(event, str) and event == "return_from_add_favorite_delete":
            pass
        else:
            if event.postback.data.lower() == "return_main":
                self.go_back_vocabulary(event)
            else:
                reply_token = event.reply_token
                flex = make_vocabulary_flex_db(event, "favorite")
                send_flex_message(reply_token, "favorite", flex)

    def is_going_to_vocabulary_add_favorite(self, event):
        if isinstance(event, PostbackEvent):
            if event.postback.data == "favorite" or event.postback.data == "test":
                return False
            else:
                level = event.postback.data.split('N')[1]
                option = event.postback.data[0]
                if level in self.state:
                    if option == 'a':
                        return True
                    if option == 't':
                        if "answer" in self.state:
                            return True
        else:
            return False

    def on_enter_vocabulary_add_favorite(self, event):
        #print("I'm entering add favorite")
        reply_token = event.reply_token
        if event.postback.data[0] == 'a':
            result = add_vocabulary_to_db(event, "vocabulary")
        else:
            result = add_vocabulary_to_db(event, "test")
        if result:
            send_text_message(reply_token, "已將單字加入收藏")
        else:
            send_text_message(reply_token, "單字已在收藏")

        level = event.postback.data.split('N')[1]
        if event.postback.data[0] == 't':
            if level == '2':
                self.go_back_vocabulary_test_type_level_2_answer("return_from_add_favorite_test_level_" + level)
            elif level == '3':
                self.go_back_vocabulary_test_type_level_3_answer("return_from_add_favorite_test_level_" + level)
            elif level == '4':
                self.go_back_vocabulary_test_type_level_4_answer("return_from_add_favorite_test_level_" + level)
            elif level == '5':
                self.go_back_vocabulary_test_type_level_5_answer("return_from_add_favorite_test_level_" + level)
        else:
            if level == '2':
                self.go_back_vocabulary_n2("return_from_add_favorite_n2")
            elif level == '3':
                self.go_back_vocabulary_n3("return_from_add_favorite_n3")
            elif level == '4':
                self.go_back_vocabulary_n4("return_from_add_favorite_n4")
            elif level == '5':
                self.go_back_vocabulary_n5("return_from_add_favorite_n5")

    def is_going_to_vocabulary_delete_favorite(self, event):
        if isinstance(event, PostbackEvent):
            option = event.postback.data[0]
            if option == 'd':
                return True
        return False

    def on_enter_vocabulary_delete_favorite(self, event):
        #print("I'm entering delete favorite")
        reply_token = event.reply_token
        result = delete_vocabulary_to_db(event)
        if result:
            send_text_message(reply_token, "已將單字移除收藏")
        else:
            send_text_message(reply_token, "單字不在收藏")
        self.go_back_favorite("return_from_add_favorite_delete");

    # def is_going_to_vocabulary_export_favorite(self, event):
    #     if not isinstance(event, PostbackEvent):
    #         return False
    #     else:
    #         if event.postback.data == 'export_favorite':
    #             return True

    # def on_enter_vocabulary_export_favorite(self, event):
    #     print("I'm entering export favorite")
    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "請輸入電子信箱")
    #
    # def is_going_to_vocabulary_export_favorite_email(self, event):
    #     if not isinstance(event, PostbackEvent):
    #         return event.message.text.find('@') != -1
    #
    # def on_enter_vocabulary_export_favorite_email(self, event):
    #     print("I'm entering input email")
    #     if event.message.text.find('@') != -1:
    #         reply_token = event.reply_token
    #         export_favorite(event)
    #         flex = after_mail()
    #         send_flex_message(reply_token, "mail_send", flex)
    #
    #
    # def is_going_to_vocabulary_export_favorite_email_complete(self, event):
    #     if event.postback.data == 'return_main':
    #         return True
    #     else:
    #         return False
    #
    # def on_enter_vocabulary_export_favorite_email_complete(self, event):
    #     print("I'm entering complete email")
    #     self.go_back_vocabulary(event)

    def is_going_to_vocabulary_test(self, event):
        if not isinstance(event, PostbackEvent):
            return False
        else:
            if event.postback.data == 'test' or event.postback.data == 'return_main':
                return True

    def on_enter_vocabulary_test(self, event):
        # print("I'm entering vocabulary test")
        if event.postback.data.lower() == "return_main":
            self.go_back_vocabulary(event)
        else:
            reply_token = event.reply_token
            flex = test_type_choose()
            send_flex_message(reply_token, "choose_type", flex)

    def is_going_to_vocabulary_test_type(self, event):
        if not isinstance(event, PostbackEvent):
            return False
        else:
            if event.postback.data == "spell" or event.postback.data == "chinese":
                return True
        return False

    def on_enter_vocabulary_test_type(self, event):
        # print("I'm entering vocabulary test type")
        reply_token = event.reply_token
        flex = test_level_choose(event.postback.data)
        send_flex_message(reply_token, "choose_level", flex)

    def is_going_to_vocabulary_test_type_level_2(self, event):
        if not isinstance(event, PostbackEvent):
            return False
        else:
            if self.state == "vocabulary_test_type_level_2_answer":
                if "next" not in event.postback.data:
                    return False
            index_level = event.postback.data.split('N')
            if "spell" in index_level[0] or "chinese" in index_level[0]:
                if index_level[1] == "2":
                    return True
            else:
                return False
        return False

    def on_enter_vocabulary_test_type_level_2(self, event):
        # print("I'm entering vocabulary test level 2")
        reply_token = event.reply_token
        flex = generate_question(event)
        send_flex_message(reply_token, "level 2 question", flex)

    def is_going_to_vocabulary_test_type_level_3(self, event):
        if not isinstance(event, PostbackEvent):
            return False
        else:
            if self.state == "vocabulary_test_type_level_3_answer":
                if "next" not in event.postback.data:
                    return False
            index_level = event.postback.data.split('N')
            if "spell" in index_level[0] or "chinese" in index_level[0]:
                if index_level[1] == "3":
                    return True
            else:
                return False
        return False

    def on_enter_vocabulary_test_type_level_3(self, event):
        # ("I'm entering vocabulary test level 3")
        reply_token = event.reply_token
        flex = generate_question(event)
        send_flex_message(reply_token, "level 3 question", flex)

    def is_going_to_vocabulary_test_type_level_4(self, event):
        if not isinstance(event, PostbackEvent):
            return False
        else:
            if self.state == "vocabulary_test_type_level_4_answer":
                if "next" not in event.postback.data:
                    return False
            index_level = event.postback.data.split('N')
            if "spell" in index_level[0] or "chinese" in index_level[0]:
                if index_level[1] == "4":
                    return True
            else:
                return False
        return False

    def on_enter_vocabulary_test_type_level_4(self, event):
        # print("I'm entering vocabulary test level 4")
        reply_token = event.reply_token
        flex = generate_question(event)
        send_flex_message(reply_token, "level 4 question", flex)

    def is_going_to_vocabulary_test_type_level_5(self, event):
        if not isinstance(event, PostbackEvent):
            return False
        else:
            if self.state == "vocabulary_test_type_level_5_answer":
                if "next" not in event.postback.data:
                    return False
            index_level = event.postback.data.split('N')
            if "spell" in index_level[0] or "chinese" in index_level[0]:
                if index_level[1] == "5":
                    return True
            else:
                return False
        return False

    def on_enter_vocabulary_test_type_level_5(self, event):
        # print("I'm entering vocabulary test level 5")
        reply_token = event.reply_token
        flex = generate_question(event)
        send_flex_message(reply_token, "level 5 question", flex)

    def is_going_to_vocabulary_test_type_level_2_answer(self, event):
        if not isinstance(event, PostbackEvent):
            if isinstance(event, str) and event == "return_from_add_favorite_test_level_2":
                return True
        else:
            if event.postback.data == "return_main" or event.postback.data == "favorite" or event.postback.data == "test":
                return False
            index_level = event.postback.data.split('N')
            if index_level[1] not in self.state:
                return False
            if "squestion" in index_level[0]:
                return True
            elif "cquestion" in index_level[0]:
                return True
        return False

    def on_enter_vocabulary_test_type_level_2_answer(self, event):
        if isinstance(event, str) and event == "return_from_add_favorite_test_level_2":
            pass
        else:
            reply_token = event.reply_token
            flex = generate_answer(event)
            send_flex_message(reply_token, "answer", flex)

    def is_going_to_vocabulary_test_type_level_3_answer(self, event):
        if not isinstance(event, PostbackEvent):
            if isinstance(event, str) and event == "return_from_add_favorite_test_level_3":
                return True
        else:
            if event.postback.data == "return_main" or event.postback.data == "favorite" or event.postback.data == "test":
                return False
            index_level = event.postback.data.split('N')
            if index_level[1] not in self.state:
                return False
            if "squestion" in index_level[0]:
                return True
            elif "cquestion" in index_level[0]:
                return True
        return False

    def on_enter_vocabulary_test_type_level_3_answer(self, event):
        if isinstance(event, str) and event == "return_from_add_favorite_test_level_3":
            pass
        else:
            reply_token = event.reply_token
            flex = generate_answer(event)
            send_flex_message(reply_token, "answer", flex)

    def is_going_to_vocabulary_test_type_level_4_answer(self, event):
        if not isinstance(event, PostbackEvent):
            if isinstance(event, str) and event == "return_from_add_favorite_test_level_4":
                return True
        else:
            if event.postback.data == "return_main" or event.postback.data == "favorite" or event.postback.data == "test":
                return False
            index_level = event.postback.data.split('N')
            if index_level[1] not in self.state:
                return False
            if "squestion" in index_level[0]:
                return True
            elif "cquestion" in index_level[0]:
                return True
        return False

    def on_enter_vocabulary_test_type_level_4_answer(self, event):
        if isinstance(event, str) and event == "return_from_add_favorite_test_level_4":
            pass
        else:
            reply_token = event.reply_token
            flex = generate_answer(event)
            send_flex_message(reply_token, "answer", flex)

    def is_going_to_vocabulary_test_type_level_5_answer(self, event):
        if not isinstance(event, PostbackEvent):
            if isinstance(event, str) and event == "return_from_add_favorite_test_level_5":
                return True
        else:
            if event.postback.data == "return_main" or event.postback.data == "favorite" or event.postback.data == "test":
                return False
            index_level = event.postback.data.split('N')
            if index_level[1] not in self.state:
                return False
            if "squestion" in index_level[0]:
                return True
            elif "cquestion" in index_level[0]:
                return True
        return False

    def on_enter_vocabulary_test_type_level_5_answer(self, event):
        if isinstance(event, str) and event == "return_from_add_favorite_test_level_5":
            pass
        else:
            reply_token = event.reply_token
            flex = generate_answer(event)
            send_flex_message(reply_token, "answer", flex)
