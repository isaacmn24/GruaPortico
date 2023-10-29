#include "actuadores.h"
bool DireccionX;
uint8_t NivelesX;
bool DireccionY;
uint8_t NivelesY;

int X = 1;
int Y = 0;

void setup() {
  SerialPi.begin(115200); 
  Serial.begin(115200);

  ConfigurarIman(int Pin);

  ConfigurarMotores(int PinMotorX, int PinMotorY, int PinDireccion, float RelacionRevTras, int PulsosRev, int Velocidad, int DistanciaEntreEspacios);
  CalibrarCero(int CalibrarX, int CalibrarY){ //Pines de los switches

  setup_sensores();
}

void loop() {
  EsperarInformacion();
  if (RecibirModo() == 1){  
    EscaneoGeneral();
    Reacomodo();
  }
  else{
    MoverMotor(X, NivelesX, DireccionX); // Moverse desde 0,0 al almacen (depende de donde se ponga)
    MoverMotor(Y, NivelesY, DireccionY);
    Patron()
  }
}

void Reacomodo(){
  while (RecibirFin() == 0){
    EsperarInformacion(); //Bucle infinito, se rompe al recibir informacion
    SegmentarInformacion(); // Me dice quien es NivelesXY y DireccionXY

    MoverMotor(X, NivelesX, DireccionX);
    MoverMotor(Y, NivelesY, DireccionY);

    delay(3000);

    BajarPiston();
    EncenderIman();

    delay(3000);

    SubirPiston();

    EsperarInformacion();
    SegmentarInformacion();

    MoverMotor(X, NivelesX, DireccionX);
    MoverMotor(Y, NivelesY, DireccionY);

    delay(3000);

    BajarPiston();
    ApagarIman();
    SubirPiston();
  }
}

void Patron(){
  //Legué al almacen
  while (RecibirFin() == 0){
    delay(3000);

    BajarPiston();
    leerColores();
    EnviarColor();

    EsperarInformacion();
    SegmentarInformacion(); //A donde voy?
    
    EncenderIman();
    delay(3000);
    SubirPiston();

    MoverMotor(X, NivelesX, DireccionX); //Voy al destino
    MoverMotor(Y, NivelesY, DireccionY);

    delay(3000);

    BajarPiston();
    ApagarIman();
    SubirPiston();

    MoverMotor(X, NivelesX, !DireccionX); //Me regreso (notese que tienen exclamacion)
    MoverMotor(Y, NivelesY, !DireccionY);
  }
}