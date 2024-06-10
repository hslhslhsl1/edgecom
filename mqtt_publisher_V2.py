# Publisher

import paho.mqtt.client as mqtt

import smbus
import time
import random

address = 0x48
bus = smbus.SMBus(1)
A0 = 0x40

BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPIC = "TEST"

def on_connect(client, userdata,rc):
    if rc==0:
        print("Connected Successfully")
    else:
        print("Connection failed, rc = "+str(rc))

def on_publish(client,userdata,mid):
    print("Message "+str(mid)+" published.")
    
mqttclient = mqtt.Client()

mqttclient.connect(BROKER_HOST, BROKER_PORT)

mqttclient.on_connect = on_connect
mqttclient.on_publish = on_publish

while True:
    #bus.write_byte(address,A0)
    #value = bus.read_byte(address)
    value = random.random()*100
    print(value)
    time.sleep(0.5)
    mqttclient.publish(TOPIC,value)