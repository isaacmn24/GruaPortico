#include <Wire.h>

#define buttonPin PA0  // Button pin on ESP32
bool buttonState = false;

void setup() {
  Wire.begin();
  
  Serial.begin(115200);

  pinMode(buttonPin, INPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin);
  Serial.println(buttonState);

  Wire.beginTransmission(0x08); // Replace with your Raspberry Pi's I2C address
  Wire.write(buttonState);
  Wire.endTransmission();

  delay(100);  // Add a small delay for stability
}
