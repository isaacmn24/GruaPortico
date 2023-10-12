//#include <SoftwareSerial.h>

#define TX PA9
#define RX PA10
//SoftwareSerial SerialPi(RX, TX);
HardwareSerial SerialPi(RX,TX);

#define buttonPin  PB11  // Button pin on STM32
byte buttonState;
byte dataToSend;

void setup() {
  SerialPi.begin(9600);
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin);
  if (buttonState == LOW) {
    dataToSend = 0x01;  // Button pressed
  } else {
    dataToSend = 0x10;  // Button not pressed
  }

  // Send button state to Raspberry Pi
  SerialPi.write(buttonState);

  // Debugging output
  Serial.print("Button State sent to Raspberry Pi: ");
  Serial.println(buttonState);

  // Delay or perform other tasks as needed
  delay(500);
}
