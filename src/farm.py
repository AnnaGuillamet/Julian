import mqtt.subscribeData as sb

class Farm(object):
    def __init__(self,cfg):
        subscribeData = sb.ClientSubscribe(cfg)

        #print(dataMqtt)
        #enclosure_check.sensorTemperatura(subcribe.pop())
        '''enclosure_Printer.sensorHumidity(subcribe.pop())
        enclosure_Printer.sensorSmoke(subcribe.pop())
        enclosure_Filament.sensorFilament(subcribe.pop())
        enclosure_Filament.sensorFilamentTemperature(subcribe.pop())
        enclosure_Filament.sensorFilamentHumidity(subcribe.pop())'''

