# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:13:06 2017

@author: matth
"""

import mysql.connector 

host="localhost"
user="root"
password="XXX"
database="test1"


def getTemperatureMeasure():
    conn = mysql.connector.connect(host, user, password, database)
    cursor = conn.cursor()
    cursor.execute("""SELECT id, date, temperature FROM temparature""")
    rows = cursor.fetchall()
    for row in rows:
        print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
    conn.close()
    
def setARIMATemperaturePrediction(date,prediction):
    conn = mysql.connector.connect(host, user, password, database)
    cursor = conn.cursor()
    data = (date, prediction)
    cursor.execute("""INSERT INTO ARIMATemperature (date, temperature) VALUES(%s, %s)""", data)
    conn.close()
    
def setLinearRegressionPrediction(date,coefficient,firstValue):
    conn = mysql.connector.connect(host, user, password, database)
    cursor = conn.cursor()
    data = (date, coefficient,firstValue)
    cursor.execute("""INSERT INTO users (date, coefficient, firstValue) VALUES(%s, %s, %s)""", data)
    conn.close()