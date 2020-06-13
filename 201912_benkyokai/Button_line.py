#coding:UTF-8
import RPi.GPIO as GPIO
import time
import requests


PIN_IN = 17
PIN_OUT = 18

url = "https://notify-api.line.me/api/notify"
token = "line notify のトークン"
headers = {"Authorization" : "Bearer "+ token}

message =  '押すな！！'
payload = {"message" :  message}
count = 0

def linemessage(num):
    if num == 1:
        r = requests.post(url ,headers = headers ,params=payload)



GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_OUT, GPIO.OUT)



try:
    while True:
        flag = GPIO.input(PIN_IN) == GPIO.HIGH
        GPIO.output(PIN_OUT, flag)
        if flag == False:
            count+=1
            print("botan on")
            linemessage(count)
        else:
            count = 0
            
        time.sleep(0.01)
except KeyboardInterrupt:
    pass
finally:

    GPIO.cleanup()


#r = requests.post(url ,headers = headers ,params=payload)
