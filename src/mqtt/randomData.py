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
    
if __name__ == '__main__':
    rand = Random()
    broken_address = "localhost"
    client = rand.getClient()
    client.connect(broken_address)

    while True:
        rand.temperature()
        rand.humidity()
        time.sleep(10)
