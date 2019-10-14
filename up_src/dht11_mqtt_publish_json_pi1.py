# Import package
import RPi.GPIO as GPIO
import dht11
import paho.mqtt.client as mqtt
import ssl
import time
import datetime
from time import gmtime, strftime

import json

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#pin 14

# Define Variables
MQTT_PORT = 8883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "pi1"	#change


MQTT_HOST = "xxxxxxxxxxxxxxxx.iot.ap-northeast-1.amazonaws.com"
# MQTT_HOST = "xxxxxxxxxxxxxx.iot.us-east-2.amazonaws.com"
CA_ROOT_CERT_FILE = "./cert/root-CA2.crt"
THING_CERT_FILE = "./cert/xxxxxxxxxx-certificate.pem.crt"
THING_PRIVATE_KEY = "./cert/xxxxxxxxxx-private.pem.key"

# Define on_publish event function
def on_publish(client, userdata, mid):
        print "Message Published..."


# Initiate MQTT Client
mqttc = mqtt.Client()

# Register publish callback function
mqttc.on_publish = on_publish

# Configure TLS Set
mqttc.tls_set(CA_ROOT_CERT_FILE, certfile=THING_CERT_FILE, keyfile=THING_PRIVATE_KEY, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)		
mqttc.loop_start()

counter = 0
message = {}

instance = dht11.DHT11(pin=14)


while True:
        sensor = instance.read()
        d = datetime.datetime.now()

        if sensor.is_valid():
                strd=d.strftime("%Y/%m/%d %H:%M:%S")
                message ={"deviceid":"dht11","timestamp":strd,"Temp(C)": sensor.temperature, "Pressure(hPa)":sensor.humidity} #
                message['count'] = counter
                messageJson = json.dumps(message)	#        print message
                mqttc.publish(MQTT_TOPIC,messageJson,1)	#
                #print message
                counter += 1
	time.sleep(1)

# Disconnect from MQTT_Broker
# mqttc.disconnect()
