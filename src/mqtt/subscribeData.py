import paho.mqtt.client as mqtt
import enclosure
import time

class ClientSubscribe():
    def __init__(self,cfg):
        self.client = mqtt.Client() #create a new instance
        self.client.on_message = self.message
        broker_address='localhost'
        self.client.connect(broker_address) #connect to broker
        self.client.subscribe("sensors/#") #Subscribing to the topic
        self.enclosure_check = enclosure.FilamentAndPrinterEnclosure(cfg)
        
        self.client.loop_forever()  #bucle

    def message(self,client,userdata,msg):
        #Printer Enclosure-Sensors
        if msg.topic == "sensors/temperature":
            temperature = str(msg.payload)
            #print(msg.topic+" "+temperature)
            self.enclosure_check.sensorTemperatura(float(temperature[2:6]))
            time.sleep(5)
            
        elif msg.topic == "sensors/humidity":
            humidity = str(msg.payload)
            #print(msg.topic+" "+humidity) 
            self.enclosure_check.sensorHumidity(float(humidity[2:6])) 
            time.sleep(5)

        elif msg.topic == "sensors/smoke":
            smoke = str(msg.payload)
            #print(msg.topic+" "+smoke)
            self.enclosure_check.sensorSmoke(smoke[1:])
            time.sleep(5)

        #Filament Storage-Sensors
        elif msg.topic == "sensors/filament":
            filament = str(msg.payload)
            #print(msg.topic+" "+filament)
            self.enclosure_check.sensorFilament(float(filament[2:6]))
            time.sleep(5)
        
        elif msg.topic == "sensors/temperatureFilament":
            temperatureFilament = str(msg.payload)
            #print(msg.topic+" "+temperatureFilament)
            self.enclosure_check.sensorFilamentTemperature(float(temperatureFilament[2:6]))
            time.sleep(5)

        elif msg.topic == "sensors/humidityFilament":
            humidityFilament = str(msg.payload)
            #print(msg.topic+" "+humidityFilament)
            self.enclosure_check.sensorFilamentHumidity(float(humidityFilament[2:6]))
            time.sleep(5)

    
    
        

     


