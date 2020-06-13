#coding:UTF-8
import requests

def main():
    url = "https://notify-api.line.me/api/notify"
    token = "line notify のトークン"
    headers = {"Authorization" : "Bearer "+ token}

    message =  'ここにメッセージを入れます'
    payload = {"message" :  message}
#    files = {"imageFile": open("test.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです。

#    r = requests.post(url ,headers = headers ,params=payload, files=files)
    r = requests.post(url ,headers = headers ,params=payload)
if __name__ == '__main__':
    main()
    
