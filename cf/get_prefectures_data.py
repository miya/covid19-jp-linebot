import requests
from time import sleep
import firebase_admin
from firebase_admin import firestore
from datetime import datetime, timedelta, timezone


# ValueError: The default Firebase app already exists.対策
if len(firebase_admin._apps) == 0:
    firebase_admin.initialize_app()
db = firestore.client()

# 都道府県の単位を合わせる用 東京 => 東京都
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

# API
api_url = "https://covid19-japan-web-api.now.sh/api/v1/prefectures"

# firestore保存用dictionary
data_dic = {
    "detail": {"update": ""},
    "prefectures": {},
    "total": {
        "total_cases": 0,
        "total_deaths": 0
    }
}


def send_data_to_firestore(Request):

    # 初期化〜
    prefectures = {}
    json_dic = {}
    total_cases = 0
    total_deaths = 0
    cnt = 0

    # 5回getして200じゃなかったら諦める
    for i in range(5):
        r = requests.get(api_url)
        s = r.status_code
        if s == 200:
            json_dic = r.json()
            break
        else:
            cnt += 1
            sleep(10)
        if cnt >= 4:
            print("データを取得できませんでした。")
            exit()

    for i in json_dic:

        # 都道府県名の単位の修正
        name_ja = i["name_ja"]
        if name_ja in t:
            i["name_ja"] = name_ja + "都"
        elif name_ja in f:
            i["name_ja"] = name_ja + "府"
        elif name_ja in k:
            i["name_ja"] = name_ja + "県"

        # 各都道府県の感染者数・死亡者数を加算
        total_cases += i["cases"]
        total_deaths += i["deaths"]

        # 都道府県名、感染者数、死亡者数を格納
        prefectures.update({
            i["name_ja"]: {
                "cases": i["cases"],
                "deaths": i["deaths"],
                "name_en": i["name_en"]
            }
        })

    # アップデート時間
    jst = timezone(timedelta(hours=+9), "JST")
    now = datetime.now(jst).strftime("%Y-%m-%d %H:%M")

    # データを格納
    data_dic.update({
        "detail": {"update": now},
        "prefectures": prefectures,
        "total": {
            "total_cases": total_cases,
            "total_deaths": total_deaths
        }
    })

    # firestoreに保存
    doc_num = str(datetime.now(jst).hour)
    if doc_num == "22":
        db.collection("data").document("before").set(data_dic)
    db.collection("data").document(doc_num).set(data_dic)
    db.collection("data").document("now").set(data_dic)


# debug
# send_data_to_firestore("ok")
