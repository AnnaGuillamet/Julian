from notifications.telegram import MyBot 
from .sensors import TemperatureSensor as s
from .actuadors import Actuador as a
import time, enum

class ActionSensor(enum.Enum):
    TemperatureEnclosure = 'Open Fan'
    HumidityEnclosure = 'Open Fan'

class Enclousure(object):
    def __init__(self,cfg = None):
        self.telegram_client = MyBot(cfg)   
        self.token = self.telegram_client.getToken
        self.chatId = self.telegram_client.getChatId
        print(self.chatId, self.token)
    
    def getClient(self):
        pass
    #def getPrinterEnclousure(self):
     #   return PrinterEnclousure(self)

class FilamentEnclousure(Enclousure):
    pass

class PrinterEnclousure(Enclousure):
    def __init__(self, telegram_client=None, token=None, chatId=None):
        #super(PrinterEnclousure, self).__init__(telegram_client, token, chatId)
        self.T = s()
        
    def sensorTemperatura(self,temperature):
        self.T_Notification = self.T.temperatureCheck(temperature)
        if self.T_Notification == 'manually':
            self.telegram_client.message('TemperatureEnclosure',temperature,ActionSensor.TemperatureEnclosure.value)
            print('Manually')

        elif self.T_Notification == 'automatic':
            self.telegram_client.getBot().sendMessage(self.chatid, "Temperature alarm, fan is activited")
            print('Automatic')