import os
import template
import create_message
from flask import Flask, request, abort
from linebot.models import (MessageEvent, TextMessage)
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)


# Flaskのインスタンス
app = Flask(__name__)

# Line Messaging API
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.environ.get("LINE_CHANNEL_SECRET")
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input_msg = event.message.text

    if input_msg == "ヘルプ":
        msg_obj = create_message.others_message(input_msg)

    elif input_msg == "支援":
        msg_obj = create_message.others_message(input_msg)

    elif input_msg == "全国":
        msg_obj = create_message.main_message(input_msg)

    elif input_msg in list(template.pref_list):
        msg_obj = create_message.main_message(input_msg)

    else:
        msg_obj = create_message.others_message(input_msg)

    line_bot_api.reply_message(event.reply_token, messages=msg_obj)


if __name__ == "__main__":
    # app.run(threaded=True)

    # デバッグ
    app.run(host="0.0.0.0", port=8080, threaded=True, debug=True)
