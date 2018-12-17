import paho.mqtt.client as mqttClient
import time
from MDW_write import sensor_Data_Handler
from test01 import sensor_test
 
#====================================== Variables ==============================================

Connected = False                       #global variable for the state of the connection
 
broker_address= "localhost"             #Broker address
port = 1883                             #Broker port
user = "root"                           #MQTT connection username
password = ""                           #MQTT connection password


#====================================== Functions ==============================================

def on_connect(client, userdata, flags, rc):        #On connection
    if rc == 0:    
        print("Connected to broker")                    
        global Connected                                #Use global variable
        Connected = True                                #Signal connection 
    else:
        print("Connection failed")                      #"Connected" variable remains false

def on_message(client, userdata, message):          #On message
    print "Message received: "  + message.payload       #call "sensor_Data_Handler"
    sensor_Data_Handler(message.payload) #message.topic, message.payload)
    
#====================================== Procedure ==============================================

client = mqttClient.Client()#"Python")              #create new instance
#client.username_pw_set(user, password=password)    #set username and password for protocol

client.on_connect= on_connect                       #attach function to callback
client.on_message= on_message                       #attach function to callback
 
client.connect(broker_address, port=port)           #connect to broker
 
client.loop_start()                         #start the loop
 
while Connected != True:                    #Wait for connection
    time.sleep(0.5)                             #Try to connect every 0,5 sec
 
client.subscribe("labo/#")                  #Client Subscribe
 
try:                                        #Wait.
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:                   #Script interrupt with CTRL+C
    print "exiting"
    client.disconnect()                         #Disconnect and stop.
    client.loop_stop()
