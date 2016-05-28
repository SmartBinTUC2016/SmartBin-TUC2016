//THIS IS DUE BIN CODE!!!
#include <Servo.h>
#include <LiquidCrystal.h>
#include <Wire.h>
#define I2CAddress 8
Servo myservo;  // create servo object to control a servo

float weight;
float raw;
float offset;
float laverage;
float raverage;
float lfill;
float rfill;
float right;
float left;
int motion;
int user;
int fill;

typedef enum {RIGHT, UP, DOWN, LEFT, SELECT, NOTHING} button;
int userselected = 0;
int transmituser = 0;
char btn[] = "NOTHING";
button pressed = NOTHING;

int pos = 0;    // variable to store the servo position

// outside motion sensor
const int motionTrig = 33;
const int motionEcho = 32;

// fill sensor left
const int leftTrig = 49;
const int leftEcho = 48;

// fill sensor right
const int rightTrig = 37;
const int rightEcho = 36;

const int led = 13;
const int servo = 52;

LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

//TWI request event handler
void requestEvent(){
  Wire.write((int)weight/6);
  Wire.write((int)fill);
  Wire.write((int)transmituser*20);
  Wire.write(0);
}


button btnpressed() {
pressed = NOTHING;

while (pressed == NOTHING) {

int x = analogRead(0);

if (x <1000 && x >700) {
  strcpy(btn,"SELECT");
  return SELECT;
}
else if (x <700 && x >500) {
  strcpy(btn,"LEFT");
  return LEFT;
}
else if (x <500 && x >200) {
  strcpy(btn,"DOWN");
  return DOWN;
}
else if (x < 200 && x > 50) {
  strcpy(btn,"UP");
  return UP;
}
else if (x < 50) {
  strcpy(btn,"RIGHT");
  return RIGHT;
}
delay(100);
}
}

//Prints user to LCD display
void printUser() {
  lcd.clear();
  lcd.setCursor(0,0);
  switch (userselected) {
    case 1 :
    lcd.print("1: friendyninja");
    break;
    case 2 :
    lcd.print("2: grassman");
    break;
    case 3 :
    lcd.print("3: cleanshark");
    break;
    case 4 :
    lcd.print("4: spaceboy");
    break;
    case 5 :
    lcd.print("5: awesomeguy");
    break;
  }

}

//User is chosen, value between 1 and 5
void selectUser() {

 userselected = 1;
 int done = 0;
 lcd.clear();

 while(!done) {
  printUser();
  pressed = btnpressed();
  switch (pressed) {
  case UP :
  if(userselected > 1) userselected--;
  break;
  case DOWN :
  if(userselected < 5) userselected++;
  break;
  case SELECT :
  done = 1;
  break;

  }
  delay(500);
 }


}
//Ultrasonic sensor distance measurment
long readDistance(int trig, int echo) {

  // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:

  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(echo, INPUT);
  return pulseIn(echo, HIGH);
}

//Bin lid open
void open() {
  pos = 140;
  myservo.write(pos);
  selectUser();
  transmituser = userselected;

  delay(1000);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("PASSWORD:");
  lcd.setCursor(0, 1);
  lcd.print("24409193");
  delay(5000);
  lcd.clear();
  lcd.print("ENJOY YOUR WIFI");
  delay(5000);
  lcd.clear();
}

//Bin lid close
void close() {
  pos = 0;
  myservo.write(pos);
  delay(10);
}

//Calibrates
void calibrate() {
    delay(500);
    int terms = 50;
    for (int i = 1; i <= terms; i++) {
    offset += analogRead(11);
    laverage += readDistance(leftTrig,leftEcho)/58;
    raverage += readDistance(rightTrig,rightEcho)/58;
    delay(100);
    }
    offset /= terms;
    laverage /= terms;
    raverage /= terms;
}





void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  Wire.begin(I2CAddress);
  Wire.onRequest(requestEvent);
  pinMode(motionTrig, OUTPUT);
  pinMode(leftTrig, OUTPUT);
  pinMode(rightTrig, OUTPUT);
  pinMode(led, OUTPUT);
  myservo.attach(servo);  // attaches the servo on pin 10 to the servo object

  lcd.begin(16, 2);
  pinMode(10,OUTPUT);
  analogWrite(10,100);
  close();
  calibrate();
}

void loop() {
  raw = ((raw+offset)*.8+.2*analogRead(11)-offset);
  weight = raw *171/27;
  if(weight <0) weight = 0;
  motion = .2*motion + .8*readDistance(motionTrig,motionEcho)/58;
  right = .9*right + .1*(readDistance(rightTrig,rightEcho)/58);
  delay(500);

  left = .9*left + .1*readDistance(leftTrig,leftEcho)/58;
  rfill = (raverage-right-2)/(raverage-2) * 100.0;
  lfill = (laverage-left-2)/(laverage-2) * 100.0;

    if(rfill <0) rfill = 0;
    if(lfill <0) lfill = 0;
    fill=(lfill+rfill)/2;

    if (motion<20 && pos == 0) {
      open();

    }
    else if (motion >20 && pos > 0){
      close();
    }
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("W: ");
    lcd.print((int)weight);
    lcd.setCursor(8,0);
    lcd.print("M: ");
    lcd.print(motion);
    lcd.setCursor(0,1);
    lcd.print("L: ");
    lcd.print((int)lfill);
    lcd.print("%");
    lcd.setCursor(8,1);
    lcd.print("R: ");
    lcd.print((int)rfill);
    lcd.print("%");
    Serial.println(userselected);
}
