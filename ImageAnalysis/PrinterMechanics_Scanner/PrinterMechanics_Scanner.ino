/*
Name:    PerlerPrinter.ino
Created:  9/4/2017 5:14:21 PM
Author: borbs
*/

#include <Servo.h>

#define RPMS                104.0
#define STEP_PIN                2
#define DIRECTION_PIN           3

#define STEPS_PER_REV         200
#define MICROSTEPS_PER_STEP     8
#define MICROSECONDS_PER_MICROSTEP   (1000000/(STEPS_PER_REV * MICROSTEPS_PER_STEP)/(RPMS / 60))

uint32_t LastStepTime = 0;
uint32_t CurrentTime = 0;

Servo dvd_down;
int joyY = A1;
int y;

int pox, poy;

int angle = 0;

void setup() {
	pinMode(DIRECTION_PIN, OUTPUT);
	pinMode(STEP_PIN, OUTPUT);
	digitalWrite(STEP_PIN, LOW);
	digitalWrite(DIRECTION_PIN, LOW);
	Serial.begin(9600);
	Serial.print("Ready");

	dvd_down.attach(10);
}


void loop() {
	pox = analogRead(A0);
	poy = analogRead(A1);
	//Serial.println(pox);
	//Serial.println(poy);

	if (pox<400)
	{
		kreni();
		digitalWrite(DIRECTION_PIN, LOW);
	}

	if (pox>600)
	{
		kreni();
		digitalWrite(DIRECTION_PIN, HIGH);
	}

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
}

void kreni()
{
	digitalWrite(STEP_PIN, HIGH);
	//delayMicroseconds((MICROSECONDS_PER_MICROSTEP * 0.9) / 2); //scanner
	delayMicroseconds(700); //DVD

	digitalWrite(STEP_PIN, LOW);
	//delayMicroseconds((MICROSECONDS_PER_MICROSTEP * 0.9) / 2); //scanner
	delayMicroseconds(700); //DVD
}
