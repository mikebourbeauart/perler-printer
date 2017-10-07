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
#define JoyV_SW                   8
#define ServoV                    10
#define JoyV_Y                    A2
#define JoyV_X                    A3

int start_pos = 100;
int end_pos = 145;
int rot_speed = 30;
int current_pos;

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
	pinMode(JoyV_SW, INPUT);
	digitalWrite(DirectionPinV_Y, LOW);
	digitalWrite(StepPinV_Y, LOW);
	digitalWrite(JoyV_SW, HIGH);

	dvd_down.attach(ServoV);
	dvd_down.write(start_pos);

	Serial.begin(9600);
	Serial.print("Ready");


}


void loop() {

	//Serial.println(analogRead(JoyH_X));
	//Serial.println(analogRead(JoyH_Y));
	//Serial.println(analogRead(JoyV_Y));
	//Serial.println(analogRead(JoyV_X));
	//Serial.println(digitalRead(JoyV_SW));

	// Big
	if (analogRead(JoyH_Y)<400)
	{
		move_stepper(StepPinH_Y, 100);
		digitalWrite(DirectionPinH_Y, LOW);
	}

	if (analogRead(JoyH_Y)>600)
	{
		move_stepper(StepPinH_Y, 100);
		digitalWrite(DirectionPinH_Y, HIGH);
	}
	
	// Scanner
	if (analogRead(JoyH_X)<400)
	{
		move_stepper(StepPinH_X, 1);
		digitalWrite(DirectionPinH_X, HIGH);
	}

	if (analogRead(JoyH_X)>600)
	{
		move_stepper(StepPinH_X, 1);
		digitalWrite(DirectionPinH_X, LOW);
	}

	// DVD
	if (analogRead(JoyV_Y)<400)
	{
		move_stepper(StepPinV_Y, 700);
		digitalWrite(DirectionPinV_Y, HIGH);
	}

	if (analogRead(JoyV_Y)>600)
	{
		move_stepper(StepPinV_Y, 700);
		digitalWrite(DirectionPinV_Y, LOW);
	}

	// Servo


	if (digitalRead(JoyV_SW) == HIGH)
	{
		//Serial.println(digitalRead(JoyV_SW));
		if (dvd_down.read() != start_pos) {
			// Slowly move back to restart
			for (int i = end_pos; i > start_pos - 1; i--) {
				dvd_down.write(i);
				delay(rot_speed);
			}
		}
	}


	if (digitalRead(JoyV_SW) == LOW)
	{
		//Serial.println(digitalRead(JoyV_SW));
		if (dvd_down.read() != end_pos) {
			for (int i = start_pos; i < end_pos + 1; i++) {
				dvd_down.write(i);
				delay(rot_speed);
				
			}
		}
	}

}

void move_stepper(int motor_pin, int delay_val) {
	digitalWrite(motor_pin, HIGH);
	delayMicroseconds(delay_val); //big motor

	digitalWrite(motor_pin, LOW);
	delayMicroseconds(delay_val); //big motor
}