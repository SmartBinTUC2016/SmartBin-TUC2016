/*
 *  This is the code the ESP8266 wifi module uses to read
 *  sensor values via I2C from the Arduino Due as well as connect
 *  to the internet and send the values in JSON to another webserver
 */

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <Wire.h>
#define I2CAddress 8


String webString = "";

byte buff[10];
int rawWeight;
int weight;
int rawLevel;
int level;
int user;




WiFiServer server(80);

//SSID and Password of wifi go here
const char* ssid     = "TPPW4G_D0D5";
const char* password = "24409193";

//Function that requests data from the Due via I2C
void getDistance(){
  // Master request Code for Two Wire Interface, ESP master
  int n = Wire.requestFrom(I2CAddress, 4);


  //Reads data byte by byte and stores in array
  for(int i=0;i<n;i++){
    buff[i]=Wire.read();
  }

  //Check to make sure weight sensor value is within a good range
  if(buff[1]<100 && buff[1]>=0){
    rawLevel=buff[1];
  }
  rawWeight=buff[0];

  /*Users are numbered from 1 to 4 however this vlaue
  is multiplied by 10 when sent from the due. This is
  done to reduce effect of random data in I2c interface.
  */

  switch (buff[2]){
    case 0:
      user=0;
      break;
    case 20:
      user = 1;
      break;
    case 40:
      user = 2;
      break;
    case 60:
      user = 3;
    case 80:
      user=4;
      break;
    case 100:
      user=5;
      break;
    }



}

void setup() {

  Serial.begin(9600);

  Wire.pins(SDA,SCL);//TWI for sensor
  Wire.begin(SDA,SCL);




  WiFi.begin(ssid,password);
  Serial.print("\n\r \n\r working to connect");

  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("This Damn Thing");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  server.begin();
  Serial.println("HTTP server started");
}

void loop(){
  getDistance();

  //Smoothing function for level and weight
  level=(0.8*level)+(0.2*rawLevel);

  weight=(0.8*weight)+(0.2*rawWeight);


  // if(rawDistance<100){
  //   distance=rawDistance;
  // }



  // Serial.println("Distance:");
  // Serial.println(distance);

  Serial.print("Weight:");
  Serial.println(weight);
  Serial.print("Level:");
  Serial.println(level);
  Serial.print("User:");
  Serial.println(user);



  WiFiClient client = server.available();
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println("Connection: close");  // the connection will be closed after completion of the response



  client.println("Refresh: 5");  // refresh the page automatically every 5 sec


  client.println();
  // client.println("<!DOCTYPE html>");
  // client.println("<html xmlns='http://www.w3.org/1999/xhtml'>");
  // client.println("<head>\n<meta charset='UTF-8'>");
  // client.println("<title>ESP8266 Distance Sensor</title>");
  // client.println("</head>\n<body>");
  // client.println("<H2>ESP8266 & HC-SR04 Sensor</H2>");
  // client.println("<H3>Distance </H3>");
  // client.println("<pre>");
  //
  // client.print("Distance (cm)  : ");
  // client.println((int)distance);

  //JSON Data written to webserver
  client.print("{\"level\":");
  client.print(level);
  client.print(",");
  client.print("\"weight\":");
  client.print(weight);
  client.print(",");
  client.print("\"user\":");
  client.print(user);
  client.print("}");
  client.println();



  delay(1000);

}
