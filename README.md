# CensorBot
Discord上で動作する検閲botです。  
NGWORDS.txtに書かれたワード(正規表現)を検出すると、それが含まれた投稿を削除し、[検閲済]などの文字列に置き換えてから投稿します。  
**ジョークbotです。**

## 環境
Python3.7以上

## 使用方法
1. `pip install -r requirements.txt`を実行してください。
1. https://discordapp.com/developers/applications/ でbotを作ります。OAuth2タブを開き、SCOPESの項目からbotを探してチェックしてください。
1. 下にスクロールし、BOT PERMISSIONからView Channels、Send Messages、Manage Messagesを探してチェックしてください。
1. SCOPESの下の方にあるURLにアクセスし、認証します。botを追加するサーバーをここで選択してください。(サーバーの管理者権限が必要です)
1. NGワードが書かれたNGWORDS.txtを作成してください。1行に1つです。正規表現が使用可能です。#で始まる行は無視されます。  
NGWORDS.txtはmain.pyと同じディレクトリに配置してください。
1. config.sample.iniにトークンを記述し、ファイル名をconfig.iniに変更してください。
1. main.pyを起動してください。

## ライセンス
MIT License
