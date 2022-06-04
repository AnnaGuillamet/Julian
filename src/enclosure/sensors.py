class Sensor(object):
    pass

#Printer Enclosure-Sensors
class TemperatureSensor(Sensor):
    def __init__(self):
        self.maximum = 32.0
        self.minim = 28.5

    def temperatureCheck(self,temperature):
        if temperature>= self.minim and temperature<= self.maximum:
            self.msg = 'Alarm Temperature-Manual'                      
        elif temperature> self.maximum:
            self.msg = 'Alarm Temperature-Automatic'
        return self.msg

class HumiditySensor(Sensor):
    def __init__(self):
        self.maximum = 65

    def humidityCheck(self,humidity):
        if humidity>= self.maximum:
            self.msg = 'Alarm Humidity'                      
        return self.msg

class SmokeSensor(Sensor):
    def __init__(self):
        self.manual = 'Medium'
        self.automatic = 'High'

    def smokeCheck(self,smoke):
        if smoke == self.manual:
            self.msg = 'Alarm Smoke-Manual' 
        elif smoke == self.automatic:
            self.msg = 'Alarm Smoke-Automatic'                     
        return self.msg

#Filament Storage-Sensors
class FilamentRunOutSensor(Sensor):
    def __init__(self):
        self.firstnotice = 20
        self.secondnotice = 10
        self.lastnotice = 5

    def filamentRunOutCheck(self,filament):
        if filament == self.firstnotice:
            self.msg = 'Alarm Filament-20' 
        elif filament < self.firstnotice and filament >= self.secondnotice:
            self.msg = 'Alarm Filament-Manual'     
        elif filament <= self.lastnotice:
            self.msg = 'Alarm Filament-AutomaticStop'                
        return self.msg

class TemperatureSensorFilament(Sensor):
    def __init__(self):
        self.maximum = 32.0

    def temperatureCheck(self,temperature):                  
        if temperature>= self.maximum:
            self.msg = 'Too much heat on filament'
        return self.msg

class HumiditySensorFilament(Sensor):
    def __init__(self):
        self.maximum = 65

    def humidityCheck(self,humidity):
        if humidity>= self.maximum:
            self.msg = 'Too much humidity on filament'                      
        return self.msg