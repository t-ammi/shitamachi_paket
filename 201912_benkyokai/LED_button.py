import RPi.GPIO as GPIO
import time

PIN_IN = 17
PIN_OUT = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_OUT, GPIO.OUT)

try:
    while True:
        flag = GPIO.input(PIN_IN) == GPIO.HIGH
        GPIO.output(PIN_OUT, flag)
        time.sleep(0.01)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    
