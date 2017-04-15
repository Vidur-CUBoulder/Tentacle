#include <Servo.h>

/*
 * Pin Servo
 * 3   0
 * 5   1
 * 6   2
 * 8   3
 * 9   4
 * 11  5
 */

 
const int baud = 9600;
const int servoCount = 6;
int servoPins[servoCount] = { 3, 5, 6, 8, 9, 11 };
Servo servos[servoCount];

int minPulseWidth = 700;
int maxPulseWidth = 1200;

void setup() {

  for (int i = 0; i < servoCount; i++) {
    servos[i].attach(servoPins[i], minPulseWidth, maxPulseWidth);
    // Debug
    Serial.print("Servo:");
    Serial.print(i);
    Serial.print(" attached to pin ");
    Serial.println(servoPins[i]);
  }

//  servos[2].attach(2, minPulseWidth, 950); // it freaked out at > 90 with regualr pulse settings

  Serial.begin(baud);
  
  Serial.print(A0);
  Serial.print("ServoControl Ready");

}
//
void loop() {

  static int v = 0;

  if ( Serial.available() ) {
    char ch = Serial.read();

    switch (ch) {
      case '0'...'9':
        v = v * 10 + ch - '0';
        Serial.print("And ");
        Serial.println(v);
        break;
      case 'A'...'F':
        v = abs(v) % 180; // Sanity check: Servo range is 0-180
        int servoId = ch - 'A';
        servos[servoId].write(v);

        // Debug
        Serial.print(servoId);
        Serial.print("=");
        Serial.println(v);
        
        v = 0;
        break;
    }
  }
  else {
//        servo1.write(90);
//        servo2.write(90);
  }

}
