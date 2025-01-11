import time
import random
from dotenv import load_dotenv
import os
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

load_dotenv()

pnconfig = PNConfiguration()
pnconfig.publish_key = os.getenv("PUB_KEY")
pnconfig.subscribe_key = os.getenv("SUB_KEY")
pnconfig.uuid = os.getenv("UUID")

pubnub = PubNub(pnconfig)

SEVERE_AQI_THRESHOLD = 100

def read_bmp_sensor():
    return round(random.uniform(15.0, 25.0), 1), round(random.uniform(1000.0, 1025.0), 1)

def read_mq135_sensor():
    return random.randint(50, 150)

def send_to_pubnub(channel, message):
    pubnub.publish().channel(channel).message(message).sync()

while True:
    temperature, pressure = read_bmp_sensor()
    aqi = read_mq135_sensor()
    data = {
        "temperature": temperature,
        "pressure": pressure,
        "aqi": aqi,
        "alert": "severe" if aqi > SEVERE_AQI_THRESHOLD else "safe"
    }
    send_to_pubnub("airquality", data)
    print("data send succefully!! ")
    time.sleep(5)
