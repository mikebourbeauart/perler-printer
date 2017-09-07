
/*
Name:    PerlerPrinter.ino
Created:  9/4/2017 5:14:21 PM
Author: borbs
*/

#define RPMS                104.0
#define STEP_PIN                2
#define DIRECTION_PIN           3

#define STEPS_PER_REV         200
#define MICROSTEPS_PER_STEP     8
#define MICROSECONDS_PER_MICROSTEP   (1000000/(STEPS_PER_REV * MICROSTEPS_PER_STEP)/(RPMS / 60))

uint32_t LastStepTime = 0;
uint32_t CurrentTime = 0;

int poz;

void setup() {
	pinMode(DIRECTION_PIN, OUTPUT);
	pinMode(STEP_PIN, OUTPUT);
	digitalWrite(STEP_PIN, LOW);
	digitalWrite(DIRECTION_PIN, LOW);
	Serial.begin(9600);
	Serial.print("Ready");
}

int angle = 0;



void loop() {
	poz = analogRead(A0);
	//Serial.println(poz);
	if (poz<400)
	{
		start();
		digitalWrite(DIRECTION_PIN, LOW);
	}

	if (poz>600)
	{
		start();
		digitalWrite(DIRECTION_PIN, HIGH);
	}
}

void start()
{
	digitalWrite(STEP_PIN, HIGH);
	delayMicroseconds(700);
	digitalWrite(STEP_PIN, LOW);
	delayMicroseconds(700);
}

