from notifications.telegram import MyBot 
from .sensors import TemperatureSensor as TempSensor
from .sensors import HumiditySensor as HumSensor
from .sensors import SmokeSensor as SmokSensor
from .sensors import FilamentRunOutSensor as FilamSensor
from .sensors import TemperatureSensorFilament as TempSensorFilam
from .sensors import HumiditySensorFilament as HumSensorFilam
from .actuadors import StepperMotor, Fan, Gate
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


class FilamentAndPrinterEnclosure(Enclousure):
    def __init__(self, cfg):
        super(FilamentAndPrinterEnclosure, self).__init__(cfg)
        self.token = cfg["telegram"]["token"]
        self.chatId = cfg["telegram"]["chat_id"]
        self.telegram_client = MyBot(self.token,self.chatId)
        self.Filam = FilamSensor()
        self.TempFilam = TempSensorFilam()
        self.HumFilam = HumSensorFilam()
        self.Temp = TempSensor()
        self.Hum = HumSensor()
        self.Smok = SmokSensor()
        self.MotorControl = StepperMotor()
        self.FanControl = Fan()
        self.GateControl = Gate()
        self.txt = "Control action applied: {}"
    
    #Filament Storage-Sensors
    def sensorFilament(self,filament):
        self.Filam_Notification = self.Filam.filamentRunOutCheck(filament)
        if self.Filam_Notification == 'Alarm Filament-20':
            self.telegram_client.getBot().sendMessage(self.chatId, "Filament alarm, 20 left")
        
        elif self.Filam_Notification == 'Alarm Filament-Manual':
            self.telegram_client.message('FilamentEnclosure',filament,ActionSensor.FilamentEnclosure.value)

        elif self.Filam_Notification == 'Alarm Filament-AutomaticStop':
            self.telegram_client.getBot().sendMessage(self.chatId, "Filament alarm, Automatic engine stop")
            result = self.MotorControl
            
    def sensorFilamentTemperature(self,tempFilam):
        self.TempFilam_Notification = self.TempFilam.temperatureCheck(tempFilam)
        if self.TempFilam_Notification == 'Too much heat on filament':
            self.telegram_client.getBot().sendMessage(self.chatId, "Too much heat on filament, fan is activated")
            result = self.FanControl

    def sensorFilamentHumidity(self,humFilam):
        self.HumFilam_Notification = self.HumFilam.temperatureCheck(humFilam)
        if self.HumFilam_Notification == 'Too much humidity on filament':
            self.telegram_client.getBot().sendMessage(self.chatId, "Too much humidity on filament, gate is opened")
            result = self.GateControl
    
    #Printer Enclosure-Sensors
    def sensorTemperatura(self,temperature):
        self.Temp_Notification = self.Temp.temperatureCheck(temperature)
        if self.Temp_Notification == 'Alarm Temperature-Manual':
            self.telegram_client.message('TemperatureEnclosure',temperature,ActionSensor.TemperatureEnclosure.value)

        elif self.Temp_Notification == 'Alarm Temperature-Automatic':
            self.telegram_client.getBot().sendMessage(self.chatId, "Temperature alarm, fan is activited")
            print(self.txt.format(self.FanControl))
            #print(self.txt.format(self.FanControl.controlFan))
    
    def sensorHumidity(self,humidity):
        self.Hum_Notification = self.Hum.humidityCheck(humidity)
        if self.Hum_Notification == 'Alarm Humidity':
            self.telegram_client.getBot().sendMessage(self.chatId, "Humidity alarm, gate is opened")
            result = self.GateControl

    def sensorSmoke(self,smoke):
        self.Smok_Notification = self.Smok.smokeCheck(smoke)
        if self.Smok_Notification == 'Alarm Smoke-Manual':
            self.telegram_client.message('SmokeEnclosure',smoke,ActionSensor.SmokeEnclosure.value)

        elif self.Smok_Notification == 'Alarm Smoke-Automatic':
            self.telegram_client.getBot().sendMessage(self.chatId, "Smoke alarm, automatic engine stop and fan is activated")
            result = self.MotorControl
            result = self.FanControl

'''class PrinterEnclosure(Enclousure):
    def __init__(self, cfg):
        super(PrinterEnclosure, self).__init__(cfg)
        self.token = cfg["telegram"]["token"]
        self.chatId = cfg["telegram"]["chat_id"]
        self.telegram_client = MyBot(self.token,self.chatId)
        self.Temp = TempSensor()
        self.Hum = HumSensor()
        self.Smok = SmokSensor()
        self.FanControl = Fan()
        self.GateControl = Gate()
        self.MotorControl = StepperMotor()

    def sensorTemperatura(self,temperature):
        self.Temp_Notification = self.Temp.temperatureCheck(temperature)
        if self.Temp_Notification == 'Alarm Temperature-Manual':
            self.telegram_client.message('TemperatureEnclosure',temperature,ActionSensor.TemperatureEnclosure.value)

        elif self.Temp_Notification == 'Alarm Temperature-Automatic':
            self.telegram_client.getBot().sendMessage(self.chatId, "Temperature alarm, fan is activited")
            result = self.FanControl

    def sensorHumidity(self,humidity):
        self.Hum_Notification = self.H.humidityCheck(humidity)
        if self.Hum_Notification == 'Alarm Humidity':
            self.telegram_client.getBot().sendMessage(self.chatId, "Humidity alarm, gate is opened")
            result = self.GateControl

    def sensorSmoke(self,smoke):
        self.Smok_Notification = self.Smok.smokeCheck(smoke)
        if self.Smok_Notification == 'Alarm Smoke-Manual':
            self.telegram_client.message('SmokeEnclosure',smoke,ActionSensor.SmokeEnclosure.value)

        elif self.Smok_Notification == 'Alarm Smoke-Automatic':
            self.telegram_client.getBot().sendMessage(self.chatId, "Smoke alarm, automatic engine stop and fan is activated")
            result = self.MotorControl
            result = self.FanControl'''
