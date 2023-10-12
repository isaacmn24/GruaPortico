#include <SPI.h>

const int buttonPin = PA0;  // Button pin on STM32
#define SS PA4  // SS pin on STM32
byte buttonState;
byte dataToSend;

void setup() {
  SPI.begin();
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
  pinMode(SS, OUTPUT);
  digitalWrite(SS, HIGH);

}

void loop() {
  buttonState = digitalRead(buttonPin);
  if (buttonState == LOW) {
    dataToSend = 0x01;  // Button pressed
  } else {
    dataToSend = 0x10;  // Button not pressed
  }

  SPI.beginTransaction(SPISettings(1000000, MSBFIRST, SPI_MODE0));
  digitalWrite(SS, LOW);  // Start SPI communication
  SPI.transfer(buttonState); // Send button state (1 byte)
  digitalWrite(SS, HIGH); // End SPI communication
  SPI.endTransaction();

  // Debugging output
  Serial.println("Button State sent to Raspberry Pi: " + String(buttonState));

  delay(500);  // Add a small delay for stability
}
