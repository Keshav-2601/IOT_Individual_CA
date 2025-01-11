import time
import random
from gpiozero import RGBLED, Buzzer

rgb_led = RGBLED(red=17, green=27, blue=22)  
buzzer = Buzzer(18)  


SEVERE_AQI_THRESHOLD = 100  # Define this value according to Irish standards

def read_bmp_sensor():
    temperature = round(random.uniform(15.0, 25.0), 1)  
    pressure = round(random.uniform(1000.0, 1025.0), 1)  
    return temperature, pressure

def read_mq135_sensor():

    aqi = random.randint(50, 150)  
    return aqi

def control_alerts(aqi):
    if aqi > SEVERE_AQI_THRESHOLD:
        rgb_led.color = (1, 0, 0)  
        buzzer.on()  
        print("Air Quality Severe! AQI:", aqi)
    else:
        rgb_led.color = (0, 1, 0) 
        buzzer.off()  
        print("Air Quality Safe. AQI:", aqi)

try:
    while True:
        
        temperature, pressure = read_bmp_sensor()
        aqi = read_mq135_sensor()

        print(f"Temperature: {temperature}°C, Pressure: {pressure} hPa, AQI: {aqi}")
        control_alerts(aqi)
        time.sleep(5)

except KeyboardInterrupt:
    print("Program stopped by user.")
    rgb_led.off()
    buzzer.off()
