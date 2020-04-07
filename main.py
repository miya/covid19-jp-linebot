import os
import textwrap
import requests
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)

pref_list = [
    "北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県",
    "福島県", "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県",
    "東京都", "神奈川県", "新潟県", "富山県", "石川県", "福井県",
    "山梨県", "長野県", "岐阜県", "静岡県", "愛知県", "三重県",
    "滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県",
    "鳥取県", "島根県", "岡山県", "広島県", "山口県", "徳島県",
    "香川県", "愛媛県", "高知県", "福岡県", "佐賀県", "長崎県",
    "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"
]

# Flaskのインスタンス
app = Flask(__name__)

# アクセストークンの設定
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.environ.get("LINE_CHANNEL_SECRET")
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# API
base_url = "https://miya.github.io/covid19-jp-api/prefectures.json"


def get_total_cases():
    data_dic = requests.get(base_url).json()
    return sum([data_dic["prefectures_data"][i]["cases"] for i in data_dic["prefectures_data"]])

def get_total_deaths():
    data_dic = requests.get(base_url).json()
    return sum([data_dic["prefectures_data"][i]["deaths"] for i in data_dic["prefectures_data"]])

def get_pref_data(pref_name):
    return requests.get(base_url).json()["prefectures_data"][pref_name]

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
        output_msg = textwrap.dedent("""
        コロナウイルスによる日本国内の感染者数、死亡者数を調べることができます。データは２時間ごとに更新されます。
        
        \"感染者数\"
        > 日本国内の感染者総数
        
        \"死亡者数\"
        > 日本国内の死亡者総数
        
        \"都道府県名\"
        > 各都道府県の感染者数と死亡者数
        🙆‍♂️ 東京都  🙅‍♂️ 東京 
        
        データ元: https://bit.ly/2RfpBGN
        ソースコード: https://bit.ly/2UNM8fZ
        作者: https://bit.ly/3aKTx5h
           """).strip() + "\n"

    elif input_msg == "感染者数":
        output_msg = "日本国内の感染者数は{}人です。".format(get_total_cases())

    elif input_msg == "死亡者数":
        output_msg = "日本国内の死亡者数は{}人です。".format(get_total_deaths())

    elif input_msg in list(pref_list):
        pref_data = get_pref_data(input_msg)
        cases_num = pref_data["cases"]
        deaths_num = pref_data["deaths"]
        output_msg = "【{}】\n感染者数: {}人 / 死亡者数: {}人".format(input_msg, cases_num, deaths_num)

    else:
        output_msg = textwrap.dedent("""
        入力された値が間違っています。
        
        \"ヘルプ\"
        > LINE BOTの詳細情報
        
        \"感染者数\"
        > 日本国内の感染者総数
        
        \"死亡者数\"
        > 日本国内の死亡者総数
        
        \"都道府県名\"
        > 各都道府県の感染者数と死亡者数
        🙆‍♂️ 東京都  🙅‍♂️ 東京
        
        ※ ダブルクォーテーションは付けないでください。
           """).strip() + "\n"

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=output_msg))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=True, debug=True)
