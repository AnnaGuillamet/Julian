#import sys
#sys.path.append('../enclosure/')
import enclosure as e

class Farm(object):
    def __init__(self,cfg):
        enclousure = e.Enclousure(cfg)
        enclousure_Printer = e.PrinterEnclousure(enclousure)
        #enclousure_Printer = enclousure.getPrinterEnclousure()
        print('inici julian')
        enclousure_Printer.sensorTemperatura(29.0)

