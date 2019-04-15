# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import json
from collections import OrderedDict
import requests

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#データ読込み pin 14
instance = dht11.DHT11(pin=14)
  

result = instance.read()
while True:
    if result.is_valid():
    
        hi=result.humidity
        tp=result.temperature

        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % tp)
        print("Humidity: %d %%" % hi)

        #time.sleep(1)
        break
    
#print(hi)  
#print(tp)
#HTTPヘッダー
headers = {
    'Content-Type': 'application/json',
}

#送信させるJSONのフォーマット
fmtdata = r'{"Temperture": 0,"Humidity": 0,"daytime":0}'
jdata = json.loads(fmtdata)

#--jsonの各パラメータにデータを格納---
#温度
jdata["Temperture"]=tp
#湿度
jdata["Humidity"]=hi
jdata["daytime"]=str(datetime.datetime.now())
print(jdata)
#json形式にして格納
json_data = json.dumps(jdata).encode("utf-8")
print(json_data)

#POSTで送信
#response = requests.post('http://192.168.11.3:8080/post',data=json_data,headers=headers)
response = requests.post('http://127.0.0.1:5000/post',data=json_data,headers=headers)    
print(response)

