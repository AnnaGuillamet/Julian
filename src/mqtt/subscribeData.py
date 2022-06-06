import paho.mqtt.client as mqtt
import enclosure

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
            print(msg.topic+" "+temperature)
            self.enclosure_check.sensorTemperatura(float(temperature[2:6]))
            
        elif msg.topic == "sensors/humidity":
            humidity = str(msg.payload)
            print(msg.topic+" "+humidity) 
            self.enclosure_check.sensorHumidity(float(humidity[2:6])) 

        elif msg.topic == "sensors/smoke":
            smoke = str(msg.payload)
            #print(msg.topic+" "+smoke)
            return(smoke)

        #Filament Storage-Sensors
        elif msg.topic == "sensors/filament":
            filament = str(msg.payload)
            #print(msg.topic+" "+filament)
            return(filament)
        
        elif msg.topic == "sensors/temperatureFilament":
            temperatureFilament = str(msg.payload)
            #print(msg.topic+" "+temperatureFilament)
            return(temperatureFilament)
        
        elif msg.topic == "sensors/humidityFilament":
            humidityFilament = str(msg.payload)
            #print(msg.topic+" "+humidityFilament)
            return(humidityFilament)


    
    
        

     


