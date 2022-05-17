#import sys
#sys.path.append('../enclosure/')
import enclosure as e

class Farm(object):
    def __init__(self,cfg):
        enclousure_Printer = e.PrinterEnclousure(cfg)
        print('inici julian')
        enclousure_Printer.sensorTemperatura(29.0)
        enclousure_Printer.sensorHumidity(70)

