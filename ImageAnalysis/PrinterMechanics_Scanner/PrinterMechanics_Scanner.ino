/*
Name:    PerlerPrinter.ino
Created:  9/4/2017 5:14:21 PM
Author: borbs
*/

#include <Servo.h>

// Horizontal axis
#define StepPinY                2
#define DirectionPinY           3
#define StepPinX                4
#define DirectionPinX           5
#define JoyH_Y                 A1
#define JoyH_X                 A0
																																																												#define JoySwitch 2 // Joystick switch connected to interrupt Pin 2 on UNO
/*
#define RPMS                104.0
#define STEPS_PER_REV         200
#define MICROSTEPS_PER_STEP     8
#define MICROSECONDS_PER_MICROSTEP   (1000000/(STEPS_PER_REV * MICROSTEPS_PER_STEP)/(RPMS / 60))
*/

Servo dvd_down;
// Define a stepper and the pins it will use

//int joyY = A1;
//int y;

//int angle = 0;


//int pos = 12600;
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
	pinMode(DirectionPinY, OUTPUT);
	pinMode(StepPinY, OUTPUT);
	digitalWrite(StepPinY, LOW);
	digitalWrite(DirectionPinY, LOW);

	// Scanner
	pinMode(DirectionPinX, OUTPUT);
	pinMode(StepPinX, OUTPUT);
	digitalWrite(StepPinX, LOW);
	digitalWrite(DirectionPinX, LOW);

	Serial.begin(9600);
	Serial.print("Ready");

	//dvd_down.attach(10);
}


void loop() {

	//Serial.println(analogRead(JoyH_X));
	//Serial.println(analogRead(JoyH_Y));
	
	if (analogRead(JoyH_Y)<400)
	{
		move_big();
		digitalWrite(DirectionPinY, LOW);
	}

	if (analogRead(JoyH_Y)>600)
	{
		move_big();
		digitalWrite(DirectionPinY, HIGH);
	}
	
	if (analogRead(JoyH_X)<400)
	{
		move_scanner();
		digitalWrite(DirectionPinX, LOW);
	}

	if (analogRead(JoyH_X)>600)
	{
		move_scanner();
		digitalWrite(DirectionPinX, HIGH);
	}

	/*
	if (poy<400)
	{
		y = joyY;
		y = map(analogRead(joyY), 0, 1023, 900, 2100);
		dvd_down.write(y);
		delay(15);
	}

	if (poy>600)
	{
		y = joyY;
		y = map(analogRead(joyY), 0, 1023, 900, 2100);
		dvd_down.write(y);
		delay(15);
	}
*/
}

void move_big() // big motor
{
	digitalWrite(StepPinY, HIGH);
	delayMicroseconds(100); //big motor

	digitalWrite(StepPinY, LOW);
	delayMicroseconds(100); //big motor
}

void move_scanner()
{
	digitalWrite(StepPinX, HIGH);
	delayMicroseconds(1); //scanner

	digitalWrite(StepPinX, LOW);
	delayMicroseconds(1); //scanner
}
/*
void move_dvd()
{
	digitalWrite(STEP_PIN, HIGH);
	delayMicroseconds(700); //DVD

	digitalWrite(STEP_PIN, LOW);
	delayMicroseconds(700); //DVD
}
*/