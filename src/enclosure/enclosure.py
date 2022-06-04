from notifications.telegram import MyBot 
from .sensors import TemperatureSensor as TempSensor
from .sensors import HumiditySensor as HumSensor
from .sensors import SmokeSensor as SmokSensor
from .sensors import FilamentRunOutSensor as FilamSensor
from .sensors import TemperatureSensorFilament as TempSensorFilam
from .sensors import HumiditySensorFilament as HumSensorFilam
from .actuadors import Actuador as a
import time, enum

class ActionSensor(enum.Enum):
    TemperatureEnclosure = 'Open Fan'
    HumidityEnclosure = 'Open Fan'
    FilamentEnclosure = 'Motor off'
    SmokeEnclosure = 'Motor off and Open Fan'

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
        self.Filam = FilamSensor()
        self.TempFilam = TempSensorFilam()
        self.HumFilam = HumSensorFilam()
    
    def sensorFilament(self,filament):
        self.Filam_Notification = self.Filam.filamentRunOutCheck(filament)
        if self.Filam_Notification == 'Alarm Filament-20':
            self.telegram_client.getBot().sendMessage(self.chatId, "Filament alarm, 20 left")
        
        elif self.Filam_Notification == 'Alarm Filament-Manual':
            self.telegram_client.message('FilamentEnclosure',filament,ActionSensor.FilamentEnclosure.value)

        elif self.Filam_Notification == 'Alarm Filament-AutomaticStop':
            self.telegram_client.getBot().sendMessage(self.chatId, "Filament alarm, Automatic engine stop")
            
    def sensorFilamentTemperature(self,tempFilam):
        self.TempFilam_Notification = self.TempFilam.temperatureCheck(tempFilam)
        if self.TempFilam_Notification == 'Too much heat on filament':
            self.telegram_client.getBot().sendMessage(self.chatId, "Too much heat on filament, fan is activated")

    def sensorFilamentHumidity(self,humFilam):
        self.HumFilam_Notification = self.HumFilam.temperatureCheck(humFilam)
        if self.HumFilam_Notification == 'Too much humidity on filament':
            self.telegram_client.getBot().sendMessage(self.chatId, "Too much humidity on filament, gate is opened")

class PrinterEnclousure(Enclousure):
    def __init__(self, cfg):
        super(PrinterEnclousure, self).__init__(cfg)
        self.token = cfg["telegram"]["token"]
        self.chatId = cfg["telegram"]["chat_id"]
        self.telegram_client = MyBot(self.token,self.chatId)
        self.Temp = TempSensor()
        self.Hum = HumSensor()
        self.Smok = SmokSensor()

    def sensorTemperatura(self,temperature):
        self.Temp_Notification = self.T.temperatureCheck(temperature)
        if self.Temp_Notification == 'Alarm Temperature-Manual':
            self.telegram_client.message('TemperatureEnclosure',temperature,ActionSensor.TemperatureEnclosure.value)

        elif self.Temp_Notification == 'Alarm Temperature-Automatic':
            self.telegram_client.getBot().sendMessage(self.chatId, "Temperature alarm, fan is activited")

    def sensorHumidity(self,humidity):
        self.Hum_Notification = self.H.humidityCheck(humidity)
        if self.Hum_Notification == 'Alarm Humidity':
            self.telegram_client.getBot().sendMessage(self.chatId, "Humidity alarm, fan is activited")

    def sensorSmoke(self,smoke):
        self.Smok_Notification = self.Smok.smokeCheck(smoke)
        if self.Smok_Notification == 'Alarm Smoke-Manual':
            self.telegram_client.message('SmokeEnclosure',smoke,ActionSensor.SmokeEnclosure.value)

        elif self.Smok_Notification == 'Alarm Smoke-Automatic':
            self.telegram_client.getBot().sendMessage(self.chatId, "Smoke alarm, automatic engine stop and fan is activated")

