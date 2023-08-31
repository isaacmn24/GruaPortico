#include <Wire.h>

const int buttonPin = 23;  // Button pin on ESP32

void setup() {
  Wire.begin(0x08);
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
}

void loop() {
  int buttonState = digitalRead(buttonPin);
  byte dataToSend;
  Serial.println(buttonState);
  if (buttonState == LOW) {
    dataToSend = 0x01;  // Button pressed
  } else {
    dataToSend = 0x10;  // Button not pressed
  }

  Wire.beginTransmission(0x08); // Replace with your Raspberry Pi's I2C address
  Wire.write(dataToSend);
  Wire.endTransmission();

  delay(100);  // Add a small delay for stability
}
