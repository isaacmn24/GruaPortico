/*
  En main se hace la comunicación con el Raspberry Pi a través del segundo canal
  de I2C (PB21 y PB22).
  Su función es brindarle la información que el RBP le solicite.

*/
// VARIABLES GLOBALES
unsigned int rgb[3];  // lista global con valores RGB medidos del sensor de color
float distancia;      // variable global para almacenar distancia medida con sensor ultrasónico
byte comunicacion;    // byte que recibirá como slave del master

// SETUP
void setup() {
  Serial.begin(115200);   // Monitor serial para debugging
  setup_sensores();
  setup_uart();
}

void loop() {
  if (Serial.available() > 0) {
    comunicacion = SerialPi.read();
    Serial.println(comunicacion);

    switch(comunicacion) {
      case 0x01:
        leerColores(rgb);
        SerialPi.write(byte(rgb[0]));
        SerialPi.write(byte(rgb[1]));
        SerialPi.write(byte(rgb[2]));
        break;
      case 0x02:

      case 0x03:

      case 0x04:

      case 0x05:

    }
  }
}
