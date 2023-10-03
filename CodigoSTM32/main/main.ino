/*
  En main se hace la comunicación con el Raspberry Pi a través del segundo canal
  de I2C (PB21 y PB22).
  Su función es brindarle la información que el RBP le solicite.

*/

// LIBRERÍAS
#include <Wire.h>

unsigned int colores[3] = {0,0,0}; // Array que guarda los valores RGB medidos

// SEGUNDO CANAL DE I2C UTILIZADO PARA COMUNICACIÓN CON RASPBERRY PI
TwoWire Wire2(PB11, PB10);

void setup() {
  Wire2.begin(0x08);    // Segundo canal I2C solo se comunica con RBP por dirección 0x08
  Serial.begin(115200);   // Monitor serial para debugging
  Serial.println("Hola");
  //setup_sensores();
}

void loop() {
  leerColores(colores);
  Serial.print("Red: "); Serial.println(colores[0]);
  Serial.print("Green: "); Serial.println(colores[1]);
  Serial.print("Blue: "); Serial.println(colores[2]);
  Serial.println();
  delay(2000);

}
