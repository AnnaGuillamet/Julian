class Sensor(object):
    pass

#Printer Enclosure-Sensors
class TemperatureSensor(Sensor):
    def __init__(self):
        self.maximum = 33.0
        self.minim = 30.5

    def temperatureCheck(self,temperature):
        if temperature>= self.minim and temperature<= self.maximum:
            self.msg = 'Alarm Temperature-Manual'                      
        elif temperature> self.maximum:
            self.msg = 'Alarm Temperature-Automatic'
        else:
            self.msg = 'Continue'
        print(f"-Result of treating the value of temperature [{temperature}]:{self.msg}") 
        return(self.msg)      

class HumiditySensor(Sensor):
    def __init__(self):
        self.maximum = 65

    def humidityCheck(self,humidity):
        if humidity>= self.maximum:
            self.msg = 'Alarm Humidity'                      
        else:
            self.msg = 'Continue' 
        print(f"-Result of treating the value of humidity [{humidity}]:{self.msg}")
        return(self.msg)  

class SmokeSensor(Sensor):
    def __init__(self):
        self.manual = "'Medium'"
        self.automatic = "'High'"

    def smokeCheck(self,smoke):
        if smoke == self.manual:
            self.msg = 'Alarm Smoke-Manual' 
        elif smoke == self.automatic:
            self.msg = 'Alarm Smoke-Automatic' 
        else:
            self.msg = 'Continue' 
        print(f"-Result of treating the value of smoke [{smoke}]:{self.msg}")                       
        return self.msg

#Filament Storage-Sensors
class FilamentRunOutSensor(Sensor):
    def __init__(self):
        self.firstnotice = 30
        self.secondnotice = 20
        self.lastnotice = 15

    def filamentRunOutCheck(self,filament):
        if filament <= self.firstnotice and filament> self.secondnotice:
            self.msg = 'Alarm Filament-FirstNotice' 
        elif filament <= self.secondnotice and filament > self.lastnotice:
            self.msg = 'Alarm Filament-Manual'     
        elif filament <= self.lastnotice:
            self.msg = 'Alarm Filament-AutomaticStop'
        else:
            self.msg = 'Continue' 
        print(f"-Result of treating the value of filament [{filament}]:{self.msg}")                 
        return self.msg

class TemperatureSensorFilament(Sensor):
    def __init__(self):
        self.maximum = 32.0

    def temperatureCheck(self,temperature):                  
        if temperature>= self.maximum:
            self.msg = 'Too much heat on filament'
        else:
            self.msg = 'Continue' 
        print(f"-Result of treating the value of temperatureFilament [{temperature}]:{self.msg}")
        return self.msg

class HumiditySensorFilament(Sensor):
    def __init__(self):
        self.maximum = 65

    def humidityCheck(self,humidity):
        if humidity>= self.maximum:
            self.msg = 'Too much humidity on filament'                      
        else:
            self.msg = 'Continue' 
        print(f"-Result of treating the value of humidityFilament [{humidity}]:{self.msg}")
        return self.msg