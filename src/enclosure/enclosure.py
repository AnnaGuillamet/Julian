from notifications.telegram import MyBot 
from .sensors import TemperatureSensor as TempSensor
from .sensors import HumiditySensor as HumSensor
from .sensors import NoiseSensor as NoisSensor
from .sensors import FilamentRunOutSensor as FilamSensor
from .actuadors import Actuador as a
import time, enum

class ActionSensor(enum.Enum):
    TemperatureEnclosure = 'Open Fan'
    HumidityEnclosure = 'Open Fan'

class Enclousure(object):
    def __init__(self,cfg = None):
        super(Enclousure, self).__init__()
        self.cfg = cfg


class FilamentEnclousure(Enclousure):
    def __init__(self, cfg):
        super(PrinterEnclousure, self).__init__(cfg)
        self.token = cfg["telegram"]["token"]
        self.chatId = cfg["telegram"]["chat_id"]
        self.telegram_client = MyBot(self.token,self.chatId)
        self.F = FilamSensor()
    
    def sensorFilament(self,filament):
        self.F_Notification = self.F.filamentRunOutCheck(filament)
        if self.F_Notification == 'Alarm Filament-20':
            self.telegram_client.getBot().sendMessage(self.chatId, "Filament alarm, 20 left")
            print('Alarm Filament-20')
            #Falta 

class PrinterEnclousure(Enclousure):
    def __init__(self, cfg):
        super(PrinterEnclousure, self).__init__(cfg)
        self.token = cfg["telegram"]["token"]
        self.chatId = cfg["telegram"]["chat_id"]
        self.telegram_client = MyBot(self.token,self.chatId)
        self.T = TempSensor()
        self.H = HumSensor()

    def sensorTemperatura(self,temperature):
        self.T_Notification = self.T.temperatureCheck(temperature)
        if self.T_Notification == 'Alarm Temperature-Manual':
            self.telegram_client.message('TemperatureEnclosure',temperature,ActionSensor.TemperatureEnclosure.value)
            print('Alarm Temperature-Manual')

        elif self.T_Notification == 'Alarm Temperature-Automatic':
            self.telegram_client.getBot().sendMessage(self.chatId, "Temperature alarm, fan is activited")
            print('Alarm Temperature-Automatic')

    def sensorHumidity(self,humidity):
        self.H_Notification = self.H.humidityCheck(humidity)
        if self.H_Notification == 'Alarm Humidity':
            self.telegram_client.getBot().sendMessage(self.chatId, "Humidity alarm, fan is activited")
            print('Alarm Humidity')