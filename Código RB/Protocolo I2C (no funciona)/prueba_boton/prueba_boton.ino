#include <Wire.h>

const int buttonPin = PA0;  // Button pin on STM32

void setup() {
  Wire.begin(0x08);
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
}

void loop() {
  byte buttonState = digitalRead(buttonPin);
  byte dataToSend;
  Serial.println(buttonState);
  if (buttonState == LOW) {
    dataToSend = 0x01;  // Button pressed
  } else {
    dataToSend = 0x10;  // Button not pressed
  }

  Wire.beginTransmission(0x08);
  Wire.write(dataToSend);
  Wire.endTransmission();

  delay(500);  // Add a small delay for stability
}
