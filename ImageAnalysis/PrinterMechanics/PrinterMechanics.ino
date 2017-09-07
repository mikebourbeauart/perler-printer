/*
Name:		PerlerPrinter.ino
Created:	9/4/2017 5:14:21 PM
Author:	borbs
*/

int poz;

void setup() {
	pinMode(3, OUTPUT);
	pinMode(2, OUTPUT);
	digitalWrite(2, LOW);
	digitalWrite(3, LOW);
	Serial.begin(9600);
	Serial.print("Ready");
}

int angle = 0;



void loop() {
	poz = analogRead(A0);
	//Serial.println(poz);
	if (poz<400)
	{
		kreni();
		digitalWrite(3, LOW);
	}

	if (poz>600)
	{
		kreni();
		digitalWrite(3, HIGH);
	}
}

void kreni()
{
	digitalWrite(2, HIGH);
	delayMicroseconds(10);
	digitalWrite(2, LOW);
	delayMicroseconds(10);
}
