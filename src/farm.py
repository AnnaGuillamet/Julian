import mqtt.subscribeData as sb

class Farm(object):
    def __init__(self,cfg):
        print("--Start MQTT")
        subscribeData = sb.ClientSubscribe(cfg)



