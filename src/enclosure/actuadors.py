
class Actuador(object):
    pass

class StepperMotor(Actuador):
    def controlMotor(command):
        if command == True:
            return "Control: Engine on"
        elif command == False:
            return "Control: Engine off"

class Fan(Actuador):
    def controlFan(command):
        if command == True:
            return "Control: Fan open"
        elif command == False:
            return "Control: Fan close"

class Gate(Actuador):
    def openGate(command):
        if command == True:
            return "Control: Gate open"
        elif command == False:
            return "Control: Gate close"

