#include "DHT.h"
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
 
LiquidCrystal_I2C lcd(0x27,16,2);  // run ic2_scanner sketch and get the IC2 address, which is 0x3f in my case,it could be 0x3f in many cases

#define DHTPIN 8 // broche ou l'on a branche le capteur
#define DHTTYPE DHT11 // DHT 11

DHT dht(DHTPIN, DHTTYPE);//déclaration du capteur

void setup()
{
 Serial.begin(9600);
 dht.begin();
 lcd.init();                      // initialize the lcd
}
void loop()
{
 delay(2000);

 int h = dht.readHumidity();//on lit l'hygrometrie
 int t = dht.readTemperature();//on lit la temperature en celsius (par defaut)

 //Affichages :
// set cursor to first line
lcd.setCursor(0, 0);

// Print a message to the LCD.
  lcd.backlight();
  lcd.print("Temp: ");
  lcd.print(t);
  lcd.setCursor(0,1);
  lcd.print("Hum: ");
  lcd.print(h);
  
 Serial.print("Humidite: ");
 Serial.print(h);
 Serial.println("%");
 Serial.print("Temperature: ");
 Serial.print(t);
 Serial.println(" °C ");
}
