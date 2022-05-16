import time

class Sensor(object):
    pass


class TemperatureSensor(Sensor):
    def __init__(self):
        self.maximum_manually = 32.0
        self.minim_manually  = 28.5

    def temperatureCheck(self,temperature):
        if temperature>= self.minim_manually  and temperature<= self.maximum_manually:
            self.msg = 'manually'                      
        elif temperature> self.maximum_manually:
            self.msg = 'automatic'
        return self.msg

class HumiditySensor(Sensor):
   pass

class NoiseSensor(Sensor):
    pass

class FilamentRunOutSensor(Sensor):
    pass



