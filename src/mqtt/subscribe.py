import paho.mqtt.client as mqtt

class ClientSubcribe():
    def __init__(self):
        self.client = mqtt.Client() #create a new instance
        self.client.on_message = self.message
        broker_address='localhost'
        self.client.connect(broker_address) #connect to broker
        self.client.subscribe("sensors/#") #Subscribing to the topic

        self.items = []

        self.client.loop_forever()  #bucle
        
    def message(self,client,userdata,msg):
        #Printer Enclosure-Sensors
        if msg.topic == "sensors/temperature":
            temperature = str(msg.payload)
            print(msg.topic+" "+temperature)

        elif msg.topic == "sensors/humidity":
            humidity = str(msg.payload)
            print(msg.topic+" "+humidity)   

        elif msg.topic == "sensors/noise":
            noise = str(msg.payload)
            print(msg.topic+" "+noise)

        #Filament Storage-Sensors
        elif msg.topic == "sensors/filament":
            filament = str(msg.payload)
            print(msg.topic+" "+filament)
        
        elif msg.topic == "sensors/temperatureFilament":
            temperatureFilament = str(msg.payload)
            print(msg.topic+" "+temperatureFilament)
        
        elif msg.topic == "sensors/humidityFilament":
            humidityFilament = str(msg.payload)
            print(msg.topic+" "+humidityFilament)

subcribe = ClientSubcribe()
