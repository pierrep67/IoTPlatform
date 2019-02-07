import win32service  
import win32serviceutil  
import win32event
import paho.mqtt.client as mqttClient
import json
import pymysql
import mysql.connector


#====================================== MQTT Variables =========================================

Connected = False                                                   #global variable for the state of the connection
 
broker_address= "127.0.0.1"                                         #Broker address
port = 1883                                                         #Broker port
user = "root"                                                       #MQTT connection username
password = ""                                                       #MQTT connection password

#====================================== MySQL Variables ========================================

hostname = 'localhost'                  #Host name               
username = 'iot'                       #username for SQL connection
password = 'iot'                           #Password for SQL connection

database = 'iot'                        #DB name
table_name = "acquisition"              #table name


#====================================== MQTT manage ============================================

def on_connect(client, userdata, flags, rd):        #On connection
    if rd == 0:                      
        global Connected                                            #Use global variable
        Connected = True                                            #Signal connection 

def on_message(client, userdata, message):          #On message
    client.publish("test", message.payload)
    sensor_Data_Handler(message.payload)                            #message.topic, message.payload)

#====================================== MySQL manage ===========================================

class DatabaseManager():
	def __init__(self):
		self.conn = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
		self.conn.commit()
		self.cur = self.conn.cursor()
		
	def add_del_update_db_record(self, sql_query, args=()):
		self.cur.execute(sql_query, args)
		self.conn.commit()
		return

	def __del__(self):
		self.cur.close()
		self.conn.close()

#================================= MySQL inject ================================================

def sensor_Data_Handler(jsonData):#Topic, jsonData):
        json_Dict = json.loads(jsonData)                #Real Json handler
        id_sensors = json_Dict['sensor_ID']                 #Split Json atributes
        date = json_Dict['timestamp']
        value = json_Dict['value']
        dimension = json_Dict['dimension']

        dbObj = DatabaseManager()                       #Initialise connection
#        dbObj.add_del_update_db_record("INSERT INTO acquisition (id_sensors, value, dimension) values (%s,%s,%s);",( 01, 23, 'C'))
        dbObj.add_del_update_db_record("INSERT INTO acquisition (id_sensors, date, value, dimension) values (%s,%s,%s, %s)",(id_sensors, date, value, dimension))      #Send message
        del dbObj                                       #Close connection
        

#====================================== Service ================================================
  
class IOT(win32serviceutil.ServiceFramework):  
    _svc_name_ = "IOT"                                              #Service name
    _svc_display_name_ = "IOT"                                      #Service display name
    _svc_description_ = "Python Test Service for IOT projec. Starts the MQTT listenner"    #Service description
      
    def __init__(self, args):  
        win32serviceutil.ServiceFramework.__init__(self,args)       
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)   #Event that listens for stop request. 
      
    def SvcDoRun(self):                             #Core content of service
        #============================== MQTT procedure =========================================
        import servicemanager
        import paho.mqtt.client as mqttClient
        import time

        rc = None
        client = mqttClient.Client()#"Python")                      #create new instance
        #client.username_pw_set(user, password=password)            #set username and password for secure protocol

        client.on_connect= on_connect                               #attach function to callback
        client.on_message= on_message                               #attach function to callback
 
        client.connect(broker_address, port=port)                   #connect to broker

        while rc != win32event.WAIT_OBJECT_0:  
            client.loop_start()                                         #start the loop

#            while Connected != True:                                    #If connected
#                time.sleep(0.5)                                             #Can't remember why I put this here... BUT IT WORKS!

            client.subscribe("labo/#")                                       #Client Subscribe
            rc = win32event.WaitForSingleObject(self.hWaitStop, 5000) 

#            try:                                                        #If not connected, sleep 1 sec and try again.
#                while True:
#                    time.sleep(1) 

        client.disconnect()                                         #Disconnect and stop.
        client.loop_stop()

          
    def SvcStop(self):                              #Called when stop requested
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING) #Tells SCM service stoping
        win32event.SetEvent(self.hWaitStop)                         #Stops service

#====================================== Main procedure ================================================                
if __name__ == '__main__':                          #the service call this program. This way we have a proper launcher
    win32serviceutil.HandleCommandLine(IOT)
