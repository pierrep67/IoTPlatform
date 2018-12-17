import json
import pymysql

#================================= SQLite Variables ============================

hostname = 'localhost'                  #Host name               
username = 'root'                       #username for SQL connection
password = ''                           #Password for SQL connection

database = 'iot'                        #DB name
table_name = "acquisition"              #table name


#================================= BDD manage class ============================

class DatabaseManager():
	def __init__(self):
		self.conn = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
		self.conn.commit()
		self.cur = self.conn.cursor()
		
	def add_del_update_db_record(self, sql_query, args=()):
		self.cur.execute(sql_query, args)
		self.conn.commit()
		return

	def __del__(self):
		self.cur.close()
		self.conn.close()

#================================= Fonctions ===================================

def sensor_Data_Handler(jsonData):#Topic, jsonData):
        json_Dict = json.loads(jsonData)                #Real Json handler
        id_sensors = json_Dict['sensor_ID']                 #Split Json atributes
        #date = json_Dict['timestamp']
        value = json_Dict['value']
        dimension = json_Dict['dimension']

        dbObj = DatabaseManager()                       #Initialise connection
#        dbObj.add_del_update_db_record("INSERT INTO acquisition (id_sensors, value, dimension) values (%s,%s,%s);",( 01, 23, 'C'))
        dbObj.add_del_update_db_record("INSERT INTO acquisition (id_sensors, value, dimension) values (%s,%s,%s);",(id_sensors, value, dimension))      #Send message
        del dbObj                                       #Close connection
