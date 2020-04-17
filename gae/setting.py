import textwrap

# メインメッセージテンプレート
main_message_template = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "",
                "size": "xxl",
                "align": "center",
                "weight": "bold",
                "color": "#5DB460"
            },
            {
                "type": "text",
                "text": "",
                "size": "xs",
                "align": "center",
                "weight": "regular",
                "color": "#A39E9E"
            },
            {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "margin": "lg",
                "contents": [
                    {
                        "type": "separator"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "感染者数",
                                "flex": 0,
                                "size": "sm",
                                "align": "center",
                                "weight": "bold",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "",
                                "flex": 1,
                                "size": "sm",
                                "align": "center",
                                "weight": "bold",
                                "color": "#CA2C2C",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "前日比",
                                "flex": 0,
                                "size": "sm",
                                "align": "center",
                                "weight": "bold",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "",
                                "flex": 1,
                                "size": "sm",
                                "align": "center",
                                "weight": "bold",
                                "color": "#CA2C2C"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "死亡者数",
                                "flex": 0,
                                "size": "sm",
                                "align": "center",
                                "weight": "bold",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "",
                                "flex": 1,
                                "size": "sm",
                                "align": "center",
                                "weight": "bold",
                                "color": "#CA2C2C",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": "前日比",
                                "flex": 0,
                                "size": "sm",
                                "align": "center",
                                "weight": "bold",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "",
                                "size": "sm",
                                "align": "center",
                                "weight": "bold",
                                "color": "#CA2C2C"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}


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
              "url": "https://user-images.githubusercontent.com/34241526/79419984-e6402c80-7ff2-11ea-9c34-bab74414de7d.jpg",
              "size": "xl"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "Kyash",
                "uri": "https://user-images.githubusercontent.com/34241526/79419984-e6402c80-7ff2-11ea-9c34-bab74414de7d.jpg"
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
help_message_template = textwrap.dedent("""
    コロナウイルスによる日本国内の感染者数・死亡者数を調べることができます。前日比はの22時を基点としています。

    🦠 全国
    > 日本国内の感染者・死亡者総数

    🦠 都道府県名
    > 各都道府県の感染者数と死亡者数
      🙆‍♂️ 東京都  🙅‍♂️ 東京
      
    ⚠️ LINEBotが使用しているデータは有志が収集しているものです。より正確な情報は厚生労働省などの公的機関が発表しているものをご確認ください。

    データ元: https://bit.ly/2RfpBGN
    ソースコード: https://bit.ly/2UNM8fZ
    作者: https://bit.ly/3aKTx5h
       """).strip() + "\n"


# 誤入力メッセージテンプレート
failure_message_template = textwrap.dedent("""
    入力された値が間違っています。

    🦠 ヘルプ
    > LINE BOTの詳細情報

    🦠 全国
    > 日本国内の感染者・死亡者総数

    🦠 都道府県名
    > 各都道府県の感染者数と死亡者数
      🙆‍♂️ 東京都  🙅‍♂️ 東京
    """).strip() + "\n"


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
