def main_message_template(data_dic):

    update = data_dic["update"]
    pref_name = data_dic["pref_name"]
    cases = data_dic["cases"]
    cases_ratio = data_dic["cases_ratio"]
    deaths = data_dic["deaths"]
    deaths_ratio = data_dic["deaths_ratio"]

    template = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "action": {
                "type": "uri",
                "label": "Action",
                "uri": "https://linecorp.com"
            },
            "contents": [
                {
                    "type": "text",
                    "text": pref_name,
                    "margin": "none",
                    "size": "xxl",
                    "align": "center",
                    "weight": "bold",
                    "color": "#4FA74A"
                },
                {
                    "type": "text",
                    "text": update,
                    "margin": "none",
                    "size": "sm",
                    "align": "center",
                    "color": "#AAAAAA"
                },
                {
                    "type": "separator"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "感染者数",
                            "size": "sm",
                            "align": "center",
                            "gravity": "center",
                            "weight": "bold",
                            "color": "#000000"
                        },
                        {
                            "type": "text",
                            "text": cases,
                            "size": "sm",
                            "align": "center",
                            "gravity": "center",
                            "weight": "bold",
                            "color": "#C82525"
                        },
                        {
                            "type": "text",
                            "text": "前日比",
                            "size": "sm",
                            "align": "center",
                            "gravity": "center",
                            "weight": "bold",
                            "color": "#000000"
                        },
                        {
                            "type": "text",
                            "text": cases_ratio,
                            "size": "sm",
                            "align": "center",
                            "gravity": "center",
                            "weight": "bold",
                            "color": "#C82525"
                        }
                    ]
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": "死亡者数",
                            "size": "sm",
                            "align": "center",
                            "gravity": "center",
                            "weight": "bold",
                            "color": "#000000"
                        },
                        {
                            "type": "text",
                            "text": deaths,
                            "size": "sm",
                            "align": "center",
                            "gravity": "center",
                            "weight": "bold",
                            "color": "#C82525"
                        },
                        {
                            "type": "text",
                            "text": "前日比",
                            "size": "sm",
                            "align": "center",
                            "gravity": "center",
                            "weight": "bold",
                            "color": "#000000"
                        },
                        {
                            "type": "text",
                            "text": deaths_ratio,
                            "size": "sm",
                            "align": "center",
                            "gravity": "center",
                            "weight": "bold",
                            "color": "#C82525"
                        }
                    ]
                },
            ]
        }
    }

    return template


# 支援メッセージテンプレート
donate_message_template = {
    "type": "bubble",
    "header": {
      "type": "box",
      "layout": "vertical",
      "flex": 0,
      "contents": [
        {
          "type": "text",
          "text": "開発者を支援する",
          "size": "xxl",
          "align": "center",
          "color": "#140C0D"
        },
        {
          "type": "separator",
          "margin": "xl"
        },
        {
          "type": "text",
          "text": "QRコードを読み取ることで開発者を支援することができます。頂いたお金は開発資金及びサーバーの維持費に当てさせて頂きます。",
          "margin": "xxl",
          "align": "start",
          "weight": "regular",
          "wrap": True
        }
      ]
    },
    "body": {
      "type": "box",
      "layout": "horizontal",
      "spacing": "xxl",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "image",
              "url": "https://user-images.githubusercontent.com/34241526/79419791-7631a680-7ff2-11ea-920b-741ee6024440.jpg",
              "size": "xl"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "PayPay",
                "uri": "https://user-images.githubusercontent.com/34241526/79419791-7631a680-7ff2-11ea-920b-741ee6024440.jpg"
              },
              "color": "#E31515",
              "margin": "md",
              "style": "primary"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "image",
              "url": "https://user-images.githubusercontent.com/34241526/84120394-bd776900-aa70-11ea-9341-8f59731e000d.jpg",
              "size": "xl"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "Kyash",
                "uri": "https://user-images.githubusercontent.com/34241526/84120394-bd776900-aa70-11ea-9341-8f59731e000d.jpg"
              },
              "color": "#0890EE",
              "margin": "md",
              "style": "primary"
            }
          ]
        }
      ]
    }
}


# ヘルプメッセージテンプレート
help_message_template = {
    "type": "bubble",
    "direction": "ltr",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "COVID-19 INFO JP",
                "size": "xl",
                "align": "center",
                "weight": "bold",
                "color": "#35991E"
            },
            {
                "type": "text",
                "text": "コロナウイルスによる日本国内の感染者数・死亡者数を調べることができます。前日比は22時を基点としています。",
                "margin": "lg",
                "align": "center",
                "gravity": "center",
                "weight": "regular",
                "wrap": True
            },
            {
                "type": "separator",
                "margin": "lg"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "日本国内の情報",
                        "align": "center",
                        "gravity": "center"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "全国",
                            "text": "全国"
                        },
                        "gravity": "center"
                    }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "都道府県別の情報",
                        "align": "center",
                        "gravity": "center"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "東京都",
                            "text": "東京都"
                        },
                        "margin": "none"
                    }
                ]
            },
            {
                "type": "separator"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "データ元",
                            "uri": "https://bit.ly/2RfpBGN"
                        },
                        "margin": "sm",
                        "height": "sm",
                        "style": "secondary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "ソースコード",
                            "uri": "https://bit.ly/2UNM8fZ"
                        },
                        "margin": "sm",
                        "height": "sm",
                        "style": "secondary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "作者Twitter",
                            "uri": "https://bit.ly/3aKTx5h"
                        },
                        "height": "sm",
                        "margin": "sm",
                        "style": "secondary"
                    }
                ]
            }
        ]
    }
}


# 誤入力メッセージテンプレート
failure_message_template = {
    "type": "bubble",
    "direction": "ltr",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "入力された値が間違っています",
                "size": "md",
                "align": "center",
                "weight": "bold"
            },
            {
                "type": "separator",
                "margin": "lg"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "日本全国の情報",
                        "align": "center",
                        "gravity": "center"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "全国",
                            "text": "全国"
                        }
                    }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "都道府別県の情報",
                        "align": "center",
                        "gravity": "center"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "東京都",
                            "text": "東京都"
                        }
                    }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "LINEbotの詳細",
                        "align": "center",
                        "gravity": "center"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "ヘルプ",
                            "text": "ヘルプ"
                        },
                        "gravity": "center"
                    }
                ]
            }
        ]
    }
}


# 都道府県リスト
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
