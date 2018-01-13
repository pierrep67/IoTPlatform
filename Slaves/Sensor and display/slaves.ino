/********************* IoT project: the slaves*****************************
 
Authors:  Pierre Balbinot: pierre.balbinot@ecam-strasbourg.eu
          Kevin Maisnil: kevin.maisnil@ecam-strasbourg.eu
         
***************************************************************************/
#include "DHT.h"
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DS3231.h>
#include "Wire.h"

#define DHTPIN 8 
#define DHTTYPE DHT22
#define DS3231_I2C_ADDRESS 0x68
                                                   
LiquidCrystal_I2C lcd(0x27,16,2);
DHT dht(DHTPIN, DHTTYPE);
DS3231  rtc(SDA, SCL);

const int R = 9;
const int G = 10;

void setup() 
{
  dht.begin();
  
  lcd.init();  
  
  pinMode(R, OUTPUT);
  analogWrite(R, 0);
  pinMode(G, OUTPUT); 
  analogWrite(G, 250);

  Wire.begin();
  rtc.begin();
  rtc.setTime(12, 0, 0);
  rtc.setDate (1, 1, 2018);

  Serial.begin(9600); 
} 

void loop()
{ 
  int h = dht.readHumidity();
  int t = dht.readTemperature();
  int smoke = analogRead(A0);
  int CO2 = analogRead(A1);

  Serial.print(rtc.getDOWStr());
  Serial.print(" ");
  Serial.print(rtc.getDateStr());
  Serial.print(" -- ");
  Serial.println(rtc.getTimeStr());

  lcd.setCursor(0, 0);
  lcd.backlight();
  lcd.print("Temperature: ");
  lcd.print(t);
  lcd.setCursor(0,1);
  lcd.print("Humidity: ");
  lcd.print(h);
  
  Serial.print("Humidite: ");
  Serial.print(h);
  Serial.println("%");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.println(" °C ");

  Serial.print("Smoke ");
  Serial.print(smoke);
  Serial.println();

  Serial.print("CO2: ");
  Serial.print(CO2);
  Serial.println();
  Serial.println();

  if (t<23 and t>17 and smoke<=360 and CO2>=400){
    analogWrite(R, 0);
    analogWrite(G, 250);
    delay(1000);
  }
  if (t>=23 or t<=17 or smoke>360 or CO2<400){
    analogWrite(R, 250);
    analogWrite(G, 0);
    delay(1000);
  }
  
  delay(1000);
}
