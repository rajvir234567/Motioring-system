#include <Wifi.h>
#include <Adafruit_BMP085.h>
#include <Adafruit_MQTT.h>
#include <Adafruit_MQTT_Client.h>


#define WLAN_SSID   "VM8751745"
#define WLAN_PASS   "smnwrmMxq4sd"

#define AIO_SERVER  "io.adafruit.com"
#define AIO_SERVERPORT   1883
#define AIO_USERNAME "Tamtap"
#define AIO_Key  "aio_ozIw67GZ2KKiwjN7Uvz5HDQeiuY0" 


WiFiClient client;


void MQTT_connect():
const int LED1 = 18;
const int led2 = 19;

float Q;
float P;

string stringone, stringtwo;

Adafruit_BMP085 BMP;

void setup(){

    serial.begin(9600);
    delay(10);
}
