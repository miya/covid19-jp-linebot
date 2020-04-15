# covid19-jp-linebot

<a href="https://lin.ee/5rrZ2Ur"><img src="https://scdn.line-apps.com/n/line_add_friends/btn/ja.png" alt="友だち追加" height="36" border="0"></a> 

🦠 コロナウイルスによる日本国内の感染者数・死亡者数の情報を取得できるLINEbot



## Demo

![](https://user-images.githubusercontent.com/34241526/79329941-99f1df80-7f53-11ea-9e6d-d125476aba58.png)



## Data Source

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

## Specification

* CloudFunctionsでAPIを叩きjsonを解析、Firestoreに書き込む
* CloudFunctionsのHTTPトリガーとしてCloudSchedulerを利用、15分ごとに発火させる
* LINEBotはメッセージを受信した際にFirestoreを読み込み、メッセージを生成し送信

![](https://user-images.githubusercontent.com/34241526/79350601-a2a5de00-7f72-11ea-94e3-3aafbe992481.png)

## Licence

[MIT LICENCE](https://github.com/miya/covid19-jp-linebot/blob/master/LICENSE) 
