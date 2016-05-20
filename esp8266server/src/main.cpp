
#include <ESP8266WiFi.h>

#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <Wire.h>
#define I2CAddress 8


String webString = "";
int distance;
float weight;
int prevDist=0;

WiFiServer server(80);

//Put SSID and Password here
const char* ssid     = "";
const char* password = "";



void getDistance(){
  Wire.requestFrom(I2CAddress, 1);

  while(Wire.available()){
    distance = Wire.read();
    Serial.println(distance);
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

//JSON Data
  client.print("{\"level\":");
  client.print(3);//Dummy Number
  client.print(",");
  client.print("\"weight\":");
  client.print(5);//Dummy Number
  client.print(",");
  client.print("\"distance\":");
  client.print(distance);
  client.print("}");
  client.println();



  delay(1000);

}
