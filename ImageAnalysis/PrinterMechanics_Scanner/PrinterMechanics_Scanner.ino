/*
Name:    PerlerPrinter.ino
Created:  9/4/2017 5:14:21 PM
Author: borbs
*/

#include <Servo.h>

// Horizontal axis
#define StepPinH_Y                2
#define DirectionPinH_Y           3
#define StepPinH_X                4
#define DirectionPinH_X           5
#define JoyH_Y                    A1
#define JoyH_X                    A0

// Vertical axis
#define StepPinV_Y                6
#define DirectionPinV_Y           7
#define JoyV_Y                    A2
#define JoyV_X                    A3
#define ServoV                    10


Servo dvd_down;



/*
void setup()
{
	stepper.setMaxSpeed(10000);
	stepper.setAcceleration(10000);
}

void loop()
{
	if (stepper.distanceToGo() == 0)
	{
		delay(500);
		pos = -pos;
		stepper.moveTo(pos); \
	}
	stepper.run();
}
*/

void setup() {
	// Big
	pinMode(DirectionPinH_Y, OUTPUT);
	pinMode(StepPinH_Y, OUTPUT);
	digitalWrite(StepPinH_Y, LOW);
	digitalWrite(DirectionPinH_Y, LOW);

	// Scanner
	pinMode(DirectionPinH_X, OUTPUT);
	pinMode(StepPinH_X, OUTPUT);
	digitalWrite(StepPinH_X, LOW);
	digitalWrite(DirectionPinH_X, LOW);

	// DVD
	pinMode(DirectionPinV_Y, OUTPUT);
	pinMode(StepPinV_Y, OUTPUT);
	digitalWrite(StepPinV_Y, LOW);
	digitalWrite(DirectionPinV_Y, LOW);

	dvd_down.attach(ServoV);

	Serial.begin(9600);
	Serial.print("Ready");


}


void loop() {

	//Serial.println(analogRead(JoyH_X));
	//Serial.println(analogRead(JoyH_Y));
	Serial.println(analogRead(JoyV_Y));
	Serial.println(analogRead(JoyV_X));

	// Big
	if (analogRead(JoyH_Y)<400)
	{
		move_big();
		digitalWrite(DirectionPinH_Y, LOW);
	}

	if (analogRead(JoyH_Y)>600)
	{
		move_big();
		digitalWrite(DirectionPinH_Y, HIGH);
	}
	
	// Scanner
	if (analogRead(JoyH_X)<400)
	{
		move_scanner();
		digitalWrite(DirectionPinH_X, HIGH);
	}

	if (analogRead(JoyH_X)>600)
	{
		move_scanner();
		digitalWrite(DirectionPinH_X, LOW);
	}

	// DVD
	if (analogRead(JoyV_Y)<400)
	{
		move_dvd();
		digitalWrite(DirectionPinV_Y, HIGH);
	}

	if (analogRead(JoyV_Y)>600)
	{
		move_dvd();
		digitalWrite(DirectionPinV_Y, LOW);
	}

	// Servo

	if (analogRead(JoyV_X)<400)
	{
		int y = map(analogRead(JoyV_X), 0, 1023, 900, 2100);
		dvd_down.write(y);
		delay(1000);
	}

	if (analogRead(JoyV_X)>600)
	{
		int y = map(analogRead(JoyV_X), 0, 1023, 900, 2100);
		dvd_down.write(y);
		delay(1000);
	}

}

void move_big() // big motor
{
	digitalWrite(StepPinH_Y, HIGH);
	delayMicroseconds(100); //big motor

	digitalWrite(StepPinH_Y, LOW);
	delayMicroseconds(100); //big motor
}

void move_scanner()
{
	digitalWrite(StepPinH_X, HIGH);
	delayMicroseconds(.01); //scanner

	digitalWrite(StepPinH_X, LOW);
	delayMicroseconds(.01); //scanner
}

void move_dvd()
{
	digitalWrite(StepPinV_Y, HIGH);
	delayMicroseconds(700); //DVD

	digitalWrite(StepPinV_Y, LOW);
	delayMicroseconds(700); //DVD
}

void move_servo()
{
	digitalWrite(StepPinV_Y, HIGH);
	delayMicroseconds(700); //DVD

	digitalWrite(StepPinV_Y, LOW);
	delayMicroseconds(700); //DVD
}