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

void SegmentarInformacion(){             // x xx x xx
  datoMover = SerialPi.read();

  DireccionX = datoMover >> 5; //Primer Bit
  NivelesX = (datoMover >> 3) & 0x03; //2-3
  DireccionY = (datoMover >> 2) & 0x01; //4
  NivelesY = datoMover & 0x03; //5-6
}

bool RecibirModo(){
  datoModo = SerialPi.read();
  return datoModo;
}

bool RecibirFin(){
  datoFin = SerialPi.read();
  return datoModo;
}

void EnviarColor(){

}

void EnviarAlerta(){
  
}