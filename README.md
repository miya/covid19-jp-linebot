# covid19-jp-linebot

<a href="https://lin.ee/5rrZ2Ur"><img src="https://scdn.line-apps.com/n/line_add_friends/btn/ja.png" alt="友だち追加" height="36" border="0"></a> 

🦠 コロナウイルスによる日本国内の感染者数・死亡者数の情報を取得できるLINEbot

## Demo

![](https://user-images.githubusercontent.com/34241526/79442825-03392780-8014-11ea-8541-0a6db3b427b3.png)

## Data Source 

![UpdateData](https://github.com/ryo-ma/covid19-japan-web-api/workflows/UpdateData/badge.svg)

[ryo-ma/covid19-japan-web-api](https://github.com/ryo-ma/covid19-japan-web-api)

使用しているデータは有志が収集しているものです。より正確な情報は[厚生労働省](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000164708_00001.html)などの公的機関が発表しているものをご確認ください。

## Features

```
全国
> 日本国内の感染者数・死亡者数・前日比を出力します

都道府県名
> 都道府県ごとの感染者数・死亡者数・前日比を出力します

ヘルプ
> LINEBotの使い方、作者、リポジトリなどの情報を出力します
```

## How it works

![](https://user-images.githubusercontent.com/34241526/80704962-83857f80-8b20-11ea-9aa3-245b6818011e.png)

1. Cloud Schedulerを使い15分間隔でCloud Functionsに対してhttpリクエストを行う
2. Cloud FunctionsでAPIからデータを取得
3. 取得したデータをCloud Firestoreに保存
4. クライアント(ユーザー)がLINEbotに対してメッセージを送信
5. App Engine上のLINEbotがCloud Firestoreからデータを取り出し返信

## Licence

[MIT LICENCE](https://github.com/miya/covid19-jp-linebot/blob/master/LICENSE) 
