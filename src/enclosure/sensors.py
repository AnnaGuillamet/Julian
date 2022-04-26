import sys
sys.path.append('../notifications/') 

from channel import MyBot 
import time
import enum

class ActionSensor(enum.Enum):
    TemperatureEnclosure = 'Open Fan'
    HumidityEnclosure = 'Open Fan'

class Sensor(object):
    pass

class TemperatureSensor(Sensor):
    def __init__(self):
        print('init1')
        self.maximum = 36.0
        self.medium = 33.0
        self.minim = 27.0
        self.telegram_client = MyBot()     

    def temperature(self,temperature):
        if temperature>= self.minim and temperature<= self.medium:
            message = message('TemperatureEnclosure',temperature,ActionSensor.TemperatureEnclosure.value)
    
        elif temperature>= self.medium and temperature<= self.maximum:
            self.telegram_client.getBot().sendMessage(2014190828, "Temperature alarm, fan is activited")

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
        time.sleep(5)

