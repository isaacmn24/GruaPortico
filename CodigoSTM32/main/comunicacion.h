byte datoMover;    // byte que recibirá como slave del master
byte datoModo;
byte datoFin;
#define TX PA9
#define RX PA10
HardwareSerial SerialPi(RX,TX);

void EsperarInformacion(){
  while(SerialPi.available() == 0){ // No hacemos nada
    if (SerialPi.available() > 0){
      break;
    }
  }
}

bool RecibirModo(){
  datoModo = SerialPi.read();
  return datoModo;
}

bool RecibirFin(){
  datoFin = SerialPi.read();
  return datoModo;
}

void EnviarColor(int color){
  SerialPi.write(color);
}

void EnviarAlerta(){
  SerialPi.write(1);
}
