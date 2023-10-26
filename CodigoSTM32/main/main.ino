/*
  En main se hace la comunicación con el Raspberry Pi a través del segundo canal
  de I2C (PB21 y PB22).
  Su función es brindarle la información que el RBP le solicite.

*/
// VARIABLES GLOBALES
unsigned int rgb[3];  // lista global con valores RGB medidos del sensor de color
float distancia;      // variable global para almacenar distancia medida con sensor ultrasónico
byte comunicacion;    // byte que recibirá como slave del master

// DEFINO LOS PINES UTILIZADOS EN EL PROTOCOLO Y LO INICIO COMO SerialPi
#define TX PA9
#define RX PA10
HardwareSerial SerialPi(RX,TX);

// SETUP
void setup() {
  SerialPi.begin(115200);       // Inicio la transmisión de datos con una velocidad alta (2 MBaudios)
  Serial.begin(115200);   // Monitor serial para debugging
  setup_sensores();
}

void loop() {
  if (SerialPi.available() > 0) {
    comunicacion = SerialPi.read();
    Serial.println(comunicacion);

    switch(comunicacion) {
      case 0x01: {
        leerColores(rgb);
        SerialPi.write(byte(rgb[0]));
        SerialPi.write(byte(rgb[1]));
        SerialPi.write(byte(rgb[2]));
      }
      break;

      case 0x02: {
        int a = 6;
      }
      break;

      case 0x03: {
        int b = 6;
      }
      break;

      case 0x04: {
        int c = 6;
      }
      break;

      case 0x05: {
        int d = 6;
      }
      break;

      case 0x06: {
        int e = 6;
      }
      break;
    }
  }
}
