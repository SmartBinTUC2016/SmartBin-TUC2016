/*
 *  This sketch demonstrates how to scan WiFi networks.
 *  The API is almost the same as with the WiFi Shield library,
 *  the most obvious difference being the different file you need to include:
 */
#include <ESP8266WiFi.h>

#include <WiFiClient.h>
#include <ESP8266WebServer.h>

String webString = "";
int distance;
int prevDist=0;

WiFiServer server(80);

const char* ssid     = "TPPW4G_D0D5";
const char* password = "24409193";



void getDistance(){
  distance=Serial.read();
}

void setup() {
  Serial.println("Hello");
  Serial.begin(115200);
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


  // server.on("/", handle_root);
  // server.on("/distance", [](){
  //   getDistance();
  //   webString="Distance: "+String((int)distance)+"cm";
  //   server.send(200,"text/plain",webString);
  // });
  server.begin();
  Serial.println("HTTP server started");
}

void loop(){
  getDistance();

  Serial.println(distance);
  WiFiClient client = server.available();
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println("Connection: close");  // the connection will be closed after completion of the response
  


  client.println("Refresh: 5");  // refresh the page automatically every 5 sec


  client.println();
  client.println("<!DOCTYPE html>");
  client.println("<html xmlns='http://www.w3.org/1999/xhtml'>");
  client.println("<head>\n<meta charset='UTF-8'>");
  client.println("<title>ESP8266 Distance Sensor</title>");
  client.println("</head>\n<body>");
  client.println("<H2>ESP8266 & HC-SR04 Sensor</H2>");
  client.println("<H3>Distance </H3>");
  client.println("<pre>");

  client.print("Distance (cm)  : ");
  client.println((int)distance);

  client.print("</body>\n</html>");
  delay(1000);

}
