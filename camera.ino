#include <Servo.h> 

Servo myservo1;
Servo myservo2;

int YAxis = 1;
int XAxis = 0;

void setup() {
    Serial.begin(9600);
    pinMode(XAxis, INPUT);
    myservo1.attach(8);
    pinMode(YAxis, INPUT); 
    myservo2.attach(9);
}
void loop() {
    int X=analogRead(XAxis);
    X=X*0.1756;
    X=180-X;
    myservo1.write(X);
   
    int Y=analogRead(YAxis);
    Y=Y*0.1466;
    myservo2.write(Y);

    Serial.print(X);
    Serial.println(Y);
}
