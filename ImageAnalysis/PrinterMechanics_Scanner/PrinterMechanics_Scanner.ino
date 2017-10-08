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
#define JoyH_X                    A0
#define JoyH_Y                    A1
#define MS1 12
#define MS2 13

// Vertical axis
#define StepPinV_Y                6
#define DirectionPinV_Y           7
#define JoyV_SW                   8
#define ServoV                    9
#define JoyV_X                    A2
#define JoyV_Y                    A3

// Servo
int init_start_pos = 100;
int init_end_pos = 145;
int start_pos = init_start_pos;
int end_pos = init_end_pos;
int rot_speed = 30;
int current_pos;

// constants won't change:
const long interval = 30;
unsigned long previousMillis = 0;
Servo dvd_down;


void setup() {
	// Big
	pinMode(DirectionPinH_Y, OUTPUT);
	pinMode(StepPinH_Y, OUTPUT);
	digitalWrite(StepPinH_Y, LOW);
	digitalWrite(DirectionPinH_Y, LOW);

	// Scanner
	pinMode(DirectionPinH_X, OUTPUT);
	pinMode(StepPinH_X, OUTPUT);
	pinMode(MS1, OUTPUT);
	pinMode(MS2, OUTPUT);
	digitalWrite(MS1, LOW); // LOW LOW == full step
	digitalWrite(MS2, LOW);
	digitalWrite(StepPinH_X, LOW);
	digitalWrite(DirectionPinH_X, LOW);

	// DVD
	pinMode(DirectionPinV_Y, OUTPUT);
	pinMode(StepPinV_Y, OUTPUT);
	digitalWrite(StepPinV_Y, LOW);
	digitalWrite(DirectionPinV_Y, LOW);
	
	
	// Servo
	pinMode(JoyV_SW, INPUT);
	digitalWrite(JoyV_SW, HIGH);
	dvd_down.attach(ServoV);
	dvd_down.write(init_start_pos);

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
	if (analogRead(JoyH_Y)<400)	{
		move_stepper(StepPinH_Y, 100);
		digitalWrite(DirectionPinH_Y, LOW);
	}

	if (analogRead(JoyH_Y)>600)	{
		move_stepper(StepPinH_Y, 100);
		digitalWrite(DirectionPinH_Y, HIGH);
	}
	
	// Scanner
	if (analogRead(JoyH_X)<400)	{
		move_stepper(StepPinH_X, 1);
		digitalWrite(DirectionPinH_X, HIGH);
	}

	if (analogRead(JoyH_X)>600)	{
		move_stepper(StepPinH_X, 1);
		digitalWrite(DirectionPinH_X, LOW);
	}

	// DVD

	if (analogRead(JoyV_Y)<400)	{
		move_stepper(StepPinV_Y, 700);
		digitalWrite(DirectionPinV_Y, HIGH);
	}

	if (analogRead(JoyV_Y)>600)	{
		move_stepper(StepPinV_Y, 700);
		digitalWrite(DirectionPinV_Y, LOW);
	}

	// Servo
	if (digitalRead(JoyV_SW) == HIGH) {
		if (dvd_down.read() != init_start_pos) {

			unsigned long currentMillis = millis();
			if (currentMillis - previousMillis >= interval) { // Execute on every interval

				previousMillis = currentMillis; // Save the last time the motor moved
				dvd_down.write(end_pos);
				//move_stepper(StepPinH_Y, 100);
				//digitalWrite(DirectionPinH_Y, LOW);
				end_pos--;
				
			}
		}
		else {
			end_pos = init_end_pos; // Reset end_pos
		}
	}




	if (digitalRead(JoyV_SW) == LOW) {
		if (dvd_down.read() != init_end_pos) {
			unsigned long currentMillis = millis();
			if (currentMillis - previousMillis >= interval) { // Execute on every interval

				previousMillis = currentMillis; // Save the last time the motor moved
				dvd_down.write(start_pos);
				start_pos++;
			}
		}
		else {
			start_pos = init_start_pos; // Reset start_pos
		}
		/*
			for (int i = start_pos; i < init_end_pos + 1; i++) {
				dvd_down.write(i);
				delay(rot_speed);
			}
		*/
		
	}
}

void move_stepper(int motor_pin, int delay_val) {
	digitalWrite(motor_pin, HIGH);
	delayMicroseconds(delay_val);

	digitalWrite(motor_pin, LOW);
	delayMicroseconds(delay_val);

}



 