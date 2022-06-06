
from unittest import result


class Actuador(object):
    pass

class StepperMotor(Actuador):
    def __init__(self,bool):
        self.bool = bool

    def controlMotor(self):
        if self.bool == True:
            print("--Control action applied: Motor off")

class Fan(Actuador):
    def __init__(self,bool):
        self.bool = bool
        
    def controlFan(self):
        if self.bool == True:
            print("--Control action applied: Fan Open")

class Gate(Actuador):
    def __init__(self,bool):
        self.bool = bool

    def openGate(self):
       if self.bool == True:
            print("--Control action applied: Gate Open")
        

