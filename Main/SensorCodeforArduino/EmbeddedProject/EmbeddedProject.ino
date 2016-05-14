#include <Servo.h>
#include <LiquidCrystal.h>
Servo myservo;  // create servo object to control a servo
int weight = 0;
int raw = 0;
// twelve servo objects can be created on most boards

typedef enum {RIGHT, UP, DOWN, LEFT, SELECT, NOTHING} button;
char btn[] = "SELECT";

button pressed = SELECT;

int pos = 0;    // variable to store the servo position

// outside motion sensor
const int motionTrig = 51;
const int motionEcho = 50;

// fill sensor left
const int leftTrig = 49;
const int leftEcho = 48;

// fill sensor right
const int rightTrig = 37;
const int rightEcho = 36;

const int led = 13;
const int servo = 52;

LiquidCrystal lcd(8, 9, 4, 5, 6, 7);
void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  pinMode(motionTrig, OUTPUT);
  pinMode(leftTrig, OUTPUT);
  pinMode(rightTrig, OUTPUT);
  pinMode(led, OUTPUT);
  myservo.attach(servo);  // attaches the servo on pin 10 to the servo object

  lcd.begin(16, 2);
  pinMode(10,OUTPUT);
  analogWrite(10,10);
}

void loop() {


  raw = raw*0.7 + (0.3*analogRead(11));
  weight = ((raw-272)*171/26);
  

  long motion = readDistance(motionTrig,motionEcho) / 58;
  long right = readDistance(rightTrig,rightEcho) / 58;
  delay(300);
  long left = readDistance(leftTrig,leftEcho) / 58;

  Serial.println(weight);
  pressed = btnpressed();
  
    if (motion<20 && pos == 0) {
      open();
    }
    else if (motion >20 && pos == 180){
      close();
    } 
  
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("w: ");
    lcd.print(weight);
    lcd.setCursor(9,1);
    lcd.print("m: ");
    lcd.print(motion);
    lcd.setCursor(0,1);
    lcd.print("l: ");
    lcd.print(left);

    lcd.setCursor(9,0);
    lcd.print("r: ");
    lcd.print(right);
}

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

void open() {
  pos = 180;
  myservo.write(pos);           
  delay(10);
}

void close() {
  pos = 0;
  myservo.write(pos);           
  delay(10);
}

button btnpressed() {

int x = analogRead(0);

if (x > 1000) {
  strcpy(btn,"NOTHING"); 
  return NOTHING;
}

else if (x <1000 && x >700) {
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
 
}
  



