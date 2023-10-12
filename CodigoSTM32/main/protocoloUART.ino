/*
  En este apartado solo se inicializa la comunicación con el master.
  Se hace asi por mayor orden en el main.
*/

// DEFINO LOS PINES UTILIZADOS EN EL PROTOCOLO Y LO INICIO COMO SerialPi
#define TX PA9
#define RX PA10

void setup_uart() {
  HardwareSerial SerialPi(RX,TX);
  SerialPi.begin(2000000);       // Inicio la transmisión de datos con una velocidad alta (2 MBaudios)
}