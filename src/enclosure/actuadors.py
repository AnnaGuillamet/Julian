
from unittest import result


class Actuador(object):
    pass

class StepperMotor(Actuador):
    def controlMotor():
        result = "Motor off"

class Fan(Actuador):
    def controlFan(bool):
        if bool == True:
            print("--Control action applied: Fan Open")

class Gate(Actuador):
    def openGate():
       return "Gate open" 
        

