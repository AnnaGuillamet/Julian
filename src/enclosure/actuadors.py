
class Actuador(object):
    pass

class StepperMotor(Actuador):
    def controlMotor():
        return "Motor off"

class Fan(Actuador):
    def controlFan():
        str1 = 'Fan Open'
        return str1

class Gate(Actuador):
    def openGate():
       return "Gate open" 
        

