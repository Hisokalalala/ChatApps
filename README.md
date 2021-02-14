# Simple-Chat-Apps
簡単なチャットアプリを作成してみました。仕様としては、ユーザー名とチャットルームの名前を入力して、2人が同じルームに入って一対一のチャットができるようになっています。同時に3人以上ルームに入ることはできないようになっており、とあるルームAにすでに2人いる場合、誰かが会話を終了してルームAを出れば、3人目が入ることができます。

## INSTALLATION
```sh
pip install -r requirements.txt
```
## How to USE
```sh
git clone https://github.com/Hisokalalala/ChatApps.git
cd ChatApps
python chat.py
```
To run this application install the requirements in a virtual environment, run `python chat.py` and visit `http://localhost:5000` on one or more browser tabs.

## LICENSE
MIT License
