import random, time
import paho.mqtt.client as mqtt
from http import client

class Random():
    def __init__(self):
        self.client = mqtt.Client("farm")
        pass
    
    def getClient(self):
        return self.client
    
    #Printer Enclosure-Sensors
    def temperature(self):
        data = round(random.uniform(25.0,36.5),1)
        print("Temperature: {}".format(data))
        self.client.publish("sensors/temperature",data)
    
    def humidity(self):
        data = round(random.uniform(20,80),1)
        print("Humidity: {}".format(data))
        self.client.publish("sensors/humidity",data)
    
    def smoke(self):
        data = random.choice(['Low','Medium','High'])
        print("Smoke: {}".format(data))
        self.client.publish("sensors/noise",data)
    
    #Filament Storage-Sensors
    def filament(self):
        data = round(random.uniform(1,100),1)
        print("Filament: {}".format(data))
        self.client.publish("sensors/filament",data)
    
    def temperatureFilament(self):
        data = round(random.uniform(25.0,36.5),1)
        print("TemperatureFilament: {}".format(data))
        self.client.publish("sensors/temperatureFilament",data)

    def humidityFilament(self):
        data = round(random.uniform(20,80),1)
        print("HumidityFilament: {}".format(data))
        self.client.publish("sensors/humidityFilament",data)
  
if __name__ == '__main__':
    rand = Random()
    broken_address = "localhost"
    client = rand.getClient()
    client.connect(broken_address)

    while True:
        rand.temperature()
        rand.humidity()
        rand.smoke()
        rand.filament()
        rand.temperatureFilament()
        rand.humidityFilament()
        time.sleep(10)
