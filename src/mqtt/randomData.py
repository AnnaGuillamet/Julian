import random, time
import paho.mqtt.client as mqtt
from http import client

class Random():
    def __init__(self):
        self.client = mqtt.Client("farm")
        pass
    
    def getClient(self):
        return self.client
    
    def humidity(self):
        data = round(random.uniform(20,80),1)
        print("Humidity: {}".format(data))
        self.client.publish("sensors/humidity",data)

    def temperature(self):
        data = round(random.uniform(25.0,36.5),1)
        print("Temperature: {}".format(data))
        self.client.publish("sensors/temperature",data)
    
    def noise(self):
        data = random.choice(['Low','Medium','High'])
        print("Smoke: {}".format(data))
        self.client.publish("sensors/noise",data)
    
    def filament(self):
        data = round(random.uniform(1,100),1)
        print("Filament: {}".format(data))
        self.client.publish("sensors/filament",data)

    
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
        time.sleep(10)
