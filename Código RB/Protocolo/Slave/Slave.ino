//Se incluye la libreria Wire para el protocolo I2C
#include <Wire.h>

void setup() {
  Wire.begin(0x8); //Se une al protocolo como escalvo con la direccion 8

  Wire.onReceive(receiveEvent); //llama a receiveEvent cuando llegan datos
}

//Esta función se ejecuta cada vez que se reciben datos del maestro
void receiveEvent(int bytes) {
  while (Wire.available()){ //recorre todos los caracteres excepto el ultimo
    char c = Wire.read(); //recibe el byte como caracter
  }
  //Llama alguna funcion para realizar los movimientos y se le envian los datos que llegaron
}

void loop(){
  delay(100)
}
