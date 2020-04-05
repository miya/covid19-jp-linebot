import os
import textwrap
import requests
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)

# 都道府県識別
pref_id_dic = {
    "北海道": "1",
    "青森県": "2",
    "岩手県": "3",
    "宮城県": "4",
    "秋田県": "5",
    "山形県": "6",
    "福島県": "7",
    "茨城県": "8",
    "栃木県": "9",
    "群馬県": "10",
    "埼玉県": "11",
    "千葉県": "12",
    "東京都": "13",
    "神奈川県": "14",
    "新潟県": "15",
    "富山県": "16",
    "石川県": "17",
    "福井県": "18",
    "山梨県": "19",
    "長野県": "20",
    "岐阜県": "21",
    "静岡県": "22",
    "愛知県": "23",
    "三重県": "24",
    "滋賀県": "25",
    "京都府": "26",
    "大阪府": "27",
    "兵庫県": "28",
    "奈良県": "29",
    "和歌山県": "30",
    "鳥取県": "31",
    "島根県": "32",
    "岡山県": "33",
    "広島県": "34",
    "山口県": "35",
    "徳島県": "36",
    "香川県": "37",
    "愛媛県": "38",
    "高知県": "39",
    "福岡県": "40",
    "佐賀県": "41",
    "長崎県": "42",
    "熊本県": "43",
    "大分県": "44",
    "宮崎県": "45",
    "鹿児島県": "46",
    "沖縄県": "47"
}

# Flaskのインスタンス
app = Flask(__name__)

# アクセストークンの設定
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.environ.get("LINE_CHANNEL_SECRET")
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# FireStore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# 都道府県県別の感染者、死亡者情報
pref_doc_ref = db.collection("prefecture")

# 国内の感染者、死亡者総数
num_doc_ref = db.collection("cases_and_deaths").document("total_num")


def get_pref_data(pref_name):
    return pref_doc_ref.document(pref_id_dic[pref_name]).get().to_dict()


def get_total_cases():
    return num_doc_ref.get().to_dict()["cases_num"]


def get_total_deaths():
    return num_doc_ref.get().to_dict()["deaths_num"]


@app.route("/", methods=["GET"])
def route():
    return "ok"


@app.route("/getjson", methods=["GET"])
def get_json():
    cases_num = 0
    deaths_num = 0

    t = ["東京"]
    f = ["大阪", "京都"]
    k = [
        "青森", "岩手", "宮城", "秋田", "山形", "福島",
        "茨城", "栃木", "群馬", "埼玉", "千葉", "神奈川",
        "新潟", "富山", "石川", "福井", "山梨", "長野", "岐阜",
        "静岡", "愛知", "三重", "滋賀", "兵庫", "奈良", "和歌山",
        "鳥取", "島根", "岡山", "広島", "山口", "徳島", "香川",
        "愛媛", "高知", "福岡", "佐賀", "長崎", "熊本", "大分",
        "宮崎", "鹿児島", "沖縄"
    ]

    base_url = "https://covid19-japan-web-api.now.sh/api/v1/prefectures"
    r = requests.get(base_url)
    json_dic = r.json()

    for i in json_dic:

        # 地方自治体の呼称を直す ex: 東京 => 東京都
        name_ja = i["name_ja"]
        if name_ja in t:
            i["name_ja"] = name_ja + "都"
        elif name_ja in f:
            i["name_ja"] = name_ja + "府"
        elif name_ja in k:
            i["name_ja"] = name_ja + "県"

        cases_num += i["cases"]
        deaths_num += i["deaths"]

        # 都道府県別の感染者、死亡者を追加
        input_pref_dic = {
            "pref_name": i["name_ja"],
            "cases_num": i["cases"],
            "deaths_num": i["deaths"]
        }
        id_ = str(i["id"])
        pref_doc_ref.document(id_).set(input_pref_dic)

    # 国内の感染者、死亡者の総数を追加
    input_num_dic = {
        "cases_num": cases_num,
        "deaths_num": deaths_num
    }
    num_doc_ref.set(input_num_dic)

    return "ok"


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
        コロナウイルスによる日本国内の感染者数、死亡者数を調べることができます。
        
        \"感染者数\"
        > 日本国内の感染者総数
        
        \"死亡者数\"
        > 日本国内の死亡者総数
        
        \"都道府県名\"
        > 各都道府県の感染者数と死亡者数
        🙆‍♂️ 東京都  🙅‍♂️ 東京 
        
        データ元: https://bit.ly/2RfpBGN
        ソースコード: https://bit.ly/39IqQES
        作者: https://bit.ly/3aKTx5h
           """).strip() + "\n"

    elif input_msg == "感染者数":
        output_msg = "日本国内の感染者数は{}人です。".format(get_total_cases())

    elif input_msg == "死亡者数":
        output_msg = "日本国内の死亡者数は{}人です。".format(get_total_deaths())

    elif input_msg in list(pref_id_dic.keys()):
        pref_data = get_pref_data(input_msg)
        pref_name = pref_data["pref_name"]
        cases_num = pref_data["cases_num"]
        deaths_num = pref_data["deaths_num"]
        output_msg = "【{}】\n感染者数: {}人 / 死亡者数: {}人".format(pref_name, cases_num, deaths_num)

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
