import os
import setting
from collections import Counter
from datetime import datetime, timedelta, timezone
from flask import Flask, request, abort
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, QuickReply,
                            QuickReplyButton, MessageAction)

# Flaskのインスタンス
app = Flask(__name__)

# Line Messaging API
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.environ.get("LINE_CHANNEL_SECRET")
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# FireBase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
col_ref = db.collection("data")

# フレックスメッセージテンプレート
flex_message_template = setting.flex_message_template

# ヘルプメッセージテンプレート
help_template = setting.help_template

# 誤送信時メッセージテンプレート
failure_template = setting.failure_template

# 都道府県名リスト
pref_list = setting.pref_list

# 現在時刻
n = str(datetime.now((timezone(timedelta(hours=+9), "JST"))).hour)
# 現在時刻+1(25時間前)
b = str(datetime.now(timezone(timedelta(hours=+10), "JST")).hour)


def get_update():
    return col_ref.document(n).get().to_dict()["detail"]["update"]


def get_total_cases():
    return col_ref.document(n).get().to_dict()["total"]["total_cases"]


def get_before_total_cases():
    return col_ref.document(b).get().to_dict()["total"]["total_cases"]


def get_total_deaths():
    return col_ref.document(n).get().to_dict()["total"]["total_deaths"]


def get_before_total_deaths():
    return col_ref.document(b).get().to_dict()["total"]["total_deaths"]


def get_pref_cases(pref_name):
    return col_ref.document(n).get().to_dict()["prefectures"][pref_name]["cases"]


def get_before_pref_cases(pref_name):
    return col_ref.document(b).get().to_dict()["prefectures"][pref_name]["cases"]


def get_pref_deaths(pref_name):
    return col_ref.document(n).get().to_dict()["prefectures"][pref_name]["deaths"]


def get_before_pref_deaths(pref_name):
    return col_ref.document(b).get().to_dict()["prefectures"][pref_name]["deaths"]


def get_top_pref():
    pref_data = {}
    pref = col_ref.document(n).get().to_dict()["prefectures"]
    [pref_data.update({i: pref[i]["cases"]}) for i in pref]
    sorted_list = [i for i, j in Counter(pref_data).most_common()][:12]
    sorted_list.insert(0, "全国")
    return sorted_list


def create_text_message(output_msg, is_exist_data=True):
    if is_exist_data:
        items = [QuickReplyButton(action=MessageAction(text=item, label=item)) for item in get_top_pref()]
        return TextSendMessage(output_msg, quick_reply=QuickReply(items=items))
    else:
        items = [QuickReplyButton(action=MessageAction(label="ヘルプ", text="ヘルプ"))]
        return TextSendMessage(output_msg, quick_reply=QuickReply(items=items))


def create_flex_message(pref_name, update, cases, before_cases, deaths, before_deaths, output_msg):
    flex_message_template["body"]["contents"][0]["text"] = pref_name  # 都道府県名
    flex_message_template["body"]["contents"][1]["text"] = update  # 更新時間
    flex_message_template["body"]["contents"][2]["contents"][1]["contents"][1]["text"] = cases  # 感染者数
    flex_message_template["body"]["contents"][2]["contents"][1]["contents"][3]["text"] = before_cases  # 感染者数前日比
    flex_message_template["body"]["contents"][2]["contents"][2]["contents"][1]["text"] = deaths  # 死亡者数
    flex_message_template["body"]["contents"][2]["contents"][2]["contents"][3]["text"] = before_deaths  # 死亡者数前日比
    items = [QuickReplyButton(action=MessageAction(text=item, label=item)) for item in get_top_pref()]
    return FlexSendMessage(alt_text=output_msg, contents=flex_message_template, quick_reply=QuickReply(items=items))


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

    # 入力された文字列を格納
    input_msg = event.message.text

    if input_msg == "ヘルプ":
        msg_obj = create_text_message(help_template)

    elif input_msg == "全国":
        update = get_update() + " 更新"
        cases = get_total_cases()
        deaths = get_total_deaths()
        before_cases = get_before_total_cases()
        before_deaths = get_before_total_deaths()
        output_msg = "【日本国内】\n感染者数: {} / 死亡者数: {}".format(cases, deaths)

        if cases >= before_cases:
            bcases = "+" + str(cases - before_cases) + "人"
        else:
            bcases = "-" + str(before_cases - cases) + "人"

        bdeaths = "+" + str(deaths - before_deaths) + "人"

        msg_obj = create_flex_message(
            pref_name="日本国内",
            update=update,
            cases=str(cases) + "人",
            before_cases=bcases,
            deaths=str(deaths) + "人",
            before_deaths=bdeaths,
            output_msg=output_msg)

    elif input_msg in list(pref_list):
        update = get_update() + " 更新"

        cases = get_pref_cases(input_msg)
        deaths = get_pref_deaths(input_msg)
        before_cases = get_before_pref_cases(input_msg)
        before_deaths = get_before_pref_deaths(input_msg)

        if cases >= before_cases:
            bcases = "+" + str(cases - before_cases) + "人"
        else:
            bcases = "-" + str(before_cases - cases) + "人"

        bdeaths = "+" + str(deaths - before_deaths) + "人"

        output_msg = "【{}】\n感染者数: {} / 死亡者数: {}".format(input_msg, cases, deaths)

        msg_obj = create_flex_message(
            pref_name=input_msg,
            update=update,
            cases=str(cases) + "人",
            before_cases=bcases,
            deaths=str(deaths) + "人",
            before_deaths=bdeaths,
            output_msg=output_msg)

    else:
        msg_obj = create_text_message(failure_template)

    line_bot_api.reply_message(event.reply_token, messages=msg_obj)


if __name__ == "__main__":
    # app.run(threaded=True)

    # デバッグ
    app.run(host="0.0.0.0", port=8080, threaded=True, debug=True)
