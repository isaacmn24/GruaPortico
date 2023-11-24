#include "comunicacion.h"
#include "sensores.h"
#include "actuadores.h"

// PIN DE INTERRUPCIÓN QUE VIENE DE LA RASPBERRY PI
#define pinInterruptor PA8    // Cambiar cuando se tenga el pin soldado

bool DireccionX;
uint8_t NivelesX;
bool DireccionY;
uint8_t NivelesY;
int colorLeido;

bool motorX = 1;
bool motorY = 0;

void setup() {
  SerialPi.begin(115200); 
  Serial.begin(115200);

  CalibrarCero();

  pinMode(pinInterruptor, INPUT);
  attachInterrupt(digitalPinToInterrupt(pinInterruptor), pararTodo, RISING);

  setup_sensores();
}

void loop() {
  EsperarInformacion();
  if (RecibirModo()){  
    EscaneoGeneral();
    Reacomodo();
  }
  else{
    MoverMotor(motorX, NivelesX, DireccionX); // Moverse desde 0,0 al almacen (depende de donde se ponga)
    MoverMotor(motorY, NivelesY, DireccionY);
    Patron();
  }
}

void Reacomodo(){
  while (RecibirFin() == 0){
    EsperarInformacion(); //Bucle infinito, se rompe al recibir informacion
    SegmentarInformacion(); // Me dice quien es NivelesXY y DireccionXY

    MoverMotor(motorX, NivelesX, DireccionX);
    MoverMotor(motorY, NivelesY, DireccionY);

    delay(3000);

    BajarPiston();
    EncenderIman();

    delay(3000);

    SubirPiston();

    EsperarInformacion();
    SegmentarInformacion();

    MoverMotor(motorX, NivelesX, DireccionX);
    MoverMotor(motorY, NivelesY, DireccionY);

    delay(3000);

    BajarPiston();
    ApagarIman();
    SubirPiston();
  }
}

void Patron(){
  //Llegué al almacen
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

    MoverMotor(motorX, NivelesX, DireccionX); //Voy al destino
    MoverMotor(motorY, NivelesY, DireccionY);

    delay(3000);

    BajarPiston();
    ApagarIman();
    SubirPiston();

    MoverMotor(motorX, NivelesX, !DireccionX); //Me regreso (notese que tienen exclamacion)
    MoverMotor(motorY, NivelesY, !DireccionY);
  }
}

void SegmentarInformacion(){             // x xx x xx
  datoMover = SerialPi.read();

  DireccionX = datoMover >> 5; //Primer Bit
  NivelesX = (datoMover >> 3) & 0x03; //2-3
  DireccionY = (datoMover >> 2) & 0x01; //4
  NivelesY = datoMover & 0x03; //5-6
}

void pararTodo() {
  while (true) {
    int i = 0;
  }
}