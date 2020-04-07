# covid19-jp-linebot
<a href="https://lin.ee/5rrZ2Ur"><img src="https://scdn.line-apps.com/n/line_add_friends/btn/ja.png" alt="友だち追加" height="36" border="0"></a>  

## Demo
<img src="https://raw.githubusercontent.com/wiki/miya/covid19-jp-linebot/images/sample.gif" width="320">

## Usage
```
感染者数
> 日本国内の感染者数を出力します

死亡者数
> 日本国内の死亡者数を出力します

都道府県名
> 入力した都道府県の感染者数と死亡者数を出力します
```

## Specification
Flaskとline-bot-sdkを使いGoogleAppEngineでホスティングしました。データは[ryo-ma/covid19-japan-web-api](https://github.com/ryo-ma/covid19-japan-web-api)のAPIを30分ごとにGithubActionsで叩き[miya/covid19-jp-api](https://github.com/miya/covid19-jp-api)のGitHubPagesで擬似的なAPIを作ったものになります。linebotにコマンドが入力された際にこの擬似APIを叩くことで、データ元のサーバーに負担がかからないようにしました。

## QR
<img src="https://user-images.githubusercontent.com/34241526/78689018-d8264800-7930-11ea-929f-53c604ade7c0.png" width="200">
