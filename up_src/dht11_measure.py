import RPi.GPIO as GPIO
import dht11
import time
import datetime
from time import gmtime, strftime

#setting timeout for 7 hours
timeout = time.time() + 60*60*7
file = open('measurments.csv','a')
#sensor = BMP280.BMP280()


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance  = dht11.DHT11(pin=14)
#writing to csv file every 30 seconds

while True:
        sensor = instance.read()
        d = datetime.datetime.now()

        if sensor.is_valid():
                strd=d.strftime("%Y/%m/%d %H:%M:%S")
	        file.write(str(time.time()) + ','+strd+',' + str(sensor.temperature) + ',' + str(sensor.humidity) + '\n')
	        print strd

        time.sleep(30)

        if time.time() > timeout:
                file.close()
                break
