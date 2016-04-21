#include <Servo.h>

Servo myservo;
const int ledPin = 13;
int pos = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin,OUTPUT);
  myservo.attach(9);
}

void loop() {
  if (Serial.available())
  {
     if (Serial.read() == '0') {
      movServo();
     } else if (Serial.read() == '1') {
      Serial.println("Hello");
     }
  }
  delay(1000);
}

void movServo() {
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}

void flash(int n) {
  for (int i = 0; i < n; i++) {
    digitalWrite(ledPin,HIGH);
    delay(100);
    digitalWrite(ledPin, LOW);
    delay(100);
  }
}

