#include "actuadores.h"
#include "sensores.h"
#include "comunicacion.h"
bool DireccionX;
uint8_t NivelesX;
bool DireccionY;
uint8_t NivelesY;
int colorLeido;

int X = 1;
int Y = 0;

void setup() {
  SerialPi.begin(115200); 
  Serial.begin(115200);

  CalibrarCero(); //Pines de los switches

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
    Patron();
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
    colorLeido = leerColores();
    EnviarColor(colorLeido);

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