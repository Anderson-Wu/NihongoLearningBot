import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackEvent
from fsm import TocMachine
from fsm import createTable
from utils import send_text_message, update_state, read_state
from state_machine import machine_diagram_states,machine_diagram_transitions
load_dotenv()


machine = {}

app = Flask(__name__, static_url_path="")

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)
createTable()
'''
@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"
    '''


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    # app.logger.info(f"Request body: {body}")
    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if event.source.user_id not in machine:
            machine[event.source.user_id] = TocMachine(states=machine_diagram_states,
                                                       transitions=machine_diagram_transitions, initial="user",
                                                       auto_transitions=False, show_conditions=True, )
        if not isinstance(event, MessageEvent) and not isinstance(event, PostbackEvent):
            continue
        # if not isinstance(event.message, TextMessage):
        #    continue
        # if not isinstance(event.message.text, str):
        #    continue
        # print(f"\nFSM STATE: {machine.state}")
        machine[event.source.user_id].state = read_state(event.source.user_id)
        response = machine[event.source.user_id].advance(event)
        if not response:
            send_text_message(event.reply_token, "Not Entering any State")
        else:
            update_state(event.source.user_id, machine[event.source.user_id].state)

    return "OK"


if __name__ == "__main__":
    #machine["g"] = TocMachine(states=machine_diagram_states, transitions=machine_diagram_transitions,initial="user", auto_transitions=False, show_conditions=True, )
    #machine["g"].get_graph().draw("fsm.png", prog="dot", format="png")
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
