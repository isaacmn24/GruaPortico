/*
  En main se hace la comunicación con el Raspberry Pi a través del segundo canal
  de I2C (PB21 y PB22).
  Su función es brindarle la información que el RBP le solicite.

*/

// LIBRERÍAS
#include <Wire.h>

// SEGUNDO CANAL DE I2C UTILIZADO PARA COMUNICACIÓN CON RASPBERRY PI
TwoWire Wire2(PB11, PB10);

// VARIABLES GLOBALES
unsigned int rgb[3];  // lista global con valores RGB medidos del sensor de color
float distancia;  // variable global para almacenar distancia medida con sensor ultrasónico

void setup() {
  //Wire2.begin(0x08);    // Segundo canal I2C solo se comunica con RBP por dirección 0x08
  Serial.begin(115200);   // Monitor serial para debugging
  setup_sensores();
}

void loop() {
  leerColores(rgb);
  Serial.print("R:"); Serial.println(rgb[0]);
  Serial.print("G:"); Serial.println(rgb[1]);
  Serial.print("B:"); Serial.println(rgb[2]);
  Serial.print("Distancia: "); Serial.println(leerDistancia());
  delay(5000);
}
