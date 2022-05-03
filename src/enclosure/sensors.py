import sys
sys.path.append('../notifications/')

from telegram import MyBot 
import time
import enum
import yaml

class ActionSensor(enum.Enum):
    TemperatureEnclosure = 'Open Fan'
    HumidityEnclosure = 'Open Fan'

class Sensor(object):
    pass

class TemperatureSensor(Sensor):
    def __init__(self):
        self.maximum_manually = 32.0
        self.minim_manually  = 28.5
        self.get_config()
        self.telegram_client = MyBot(self.cfg)
        self.chatId = self.telegram_client.getChatId()   

    def get_config(self):
        with open(r"julian.yaml") as f:
            self.cfg = yaml.full_load(f)

    def temperature(self,temperature):
        if temperature>= self.minim_manually  and temperature<= self.maximum_manually:
            msg = self.telegram_client.message('TemperatureEnclosure',temperature,ActionSensor.TemperatureEnclosure.value)
    
        elif temperature> self.maximum_manually:
            self.telegram_client.getBot().sendMessage(self.chatId, "Temperature alarm, fan is activited")

class HumiditySensor(Sensor):
   pass

class SmokeSensor(Sensor):
    pass

class FilamentRunOutSensor(Sensor):
    pass

if __name__ == '__main__':
    sensor_temp = TemperatureSensor()
    print('inici sensor')
    sensor_temp.temperature(29.0)

    while 1:
        time.sleep(10)

