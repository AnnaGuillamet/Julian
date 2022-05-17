import time

class Sensor(object):
    pass


class TemperatureSensor(Sensor):
    def __init__(self):
        self.maximum_manually = 32.0
        self.minim_manually  = 28.5

    def temperatureCheck(self,temperature):
        if temperature>= self.minim_manually  and temperature<= self.maximum_manually:
            self.msg = 'Alarm Temperature-Manual'                      
        elif temperature> self.maximum_manually:
            self.msg = 'Alarm Temperature-Automatic'
        return self.msg

class HumiditySensor(Sensor):
    def __init__(self):
        self.maximum = 65

    def humidityCheck(self,humidity):
        if humidity>= self.maximum:
            self.msg = 'Alarm Humidity'                      
        return self.msg

class NoiseSensor(Sensor):
    def __init__(self):
        self.manual = 'Medium'
        self.automatic = 'High'

    def noiseCheck(self,noise):
        if noise == self.manual:
            self.msg = 'Alarm Noise-Manual' 
        elif noise == self.automatic:
            self.msg = 'Alarm Noise-Automatic'                     
        return self.msg

class FilamentRunOutSensor(Sensor):
    def __init__(self):
        self.firstnotice = 20
        self.secondnotice = 10
        self.lastnotice = 5

    def filamentRunOutCheck(self,filament):
        if filament == self.firstnotice:
            self.msg = 'Alarm Filament-20' 
        elif filament < self.firstnotice and filament >= self.secondnotice:
            self.msg = 'Alarm Noise-10-Manual'     
        elif filament <= self.lastnotice:
            self.msg = 'Alarm Filament-AutomaticStop'                
        return self.msg



