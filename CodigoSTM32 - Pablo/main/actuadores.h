#include "sensores.h"
#include "comunicacion.h"

int MotorX = 0;
int MotorY = 0;
int PinDir = 0;
int PulRev = 0;
int Vel = 0; //DelayMicroseconds - 50 funciona "bien"
int Distancia = 0; // cm
float RelRevTras = 0; // 1 revolución = ? cm lineales

//Para mover motores
bool X, Derecha, Abajo = 1; //No se si será así, hay que probar en planta
bool Y, Izquierda, Arriba = 0;

int PinIman = 0;

void ConfigurarMotores(int PinMotorX, int PinMotorY, int PinDireccion, float RelacionRevTras, int PulsosRev, int Velocidad, int DistanciaEntreEspacios){
  MotorX = PinMotorX;
  MotorY = PinMotorY;
  PinDir = PinDireccion;
  PulRev = PulsosRev;
  RelRevTras = RelacionRevTras;
  Vel = Velocidad;
  Distancia = DistanciaEntreEspacios;
}

void CalibrarCero(int CalibrarX, int CalibrarY){
  digitalWrite(PinDir, 0); //Izquierda y arriba
  while(digitalRead(CalibrarX) == 0){
    digitalWrite(MotorX, HIGH); 
    delayMicroseconds(Vel); 
    digitalWrite(MotorX, LOW); 
    delayMicroseconds(Vel);
  }
  while(digitalRead(CalibrarY) == 0){
    digitalWrite(MotorY, HIGH); 
    delayMicroseconds(Vel); 
    digitalWrite(MotorY, LOW); 
    delayMicroseconds(Vel);
  }
}

void MoverMotor(int Motor, int Nivel, bool Direccion){
  float cantRev = Nivel*Distancia/RelRevTras;
  int cantPulsos = cantRev*PulRev;

  int Tipo;         //Definimos que motor mover
  if (Motor == 1){
    Tipo = MotorX;
  }
  else {
    Tipo = MotorY;
  }

  digitalWrite(PinDir, Direccion); // Enables the motor to move in a particular direction
  for(int x = 0; x < cantPulsos; x++) {
    digitalWrite(Tipo, HIGH); 
    delayMicroseconds(Vel); 
    digitalWrite(Tipo, LOW); 
    delayMicroseconds(Vel); 
  }

}

void EscaneoGeneral(){ //Asumiendo inicio en esquina superior izquierda
  BajarPiston();
  for (int u = 0; u <= 4; u++){
    MoverMotor(Y, u, Abajo);
    for (int i = 0; i <= 4; i++){

      if (alarmaDistancia == 1){
        ParenTodo();
      }

      leerColores(); //cuanto tiempo debe estar aquí? un delay no lo va a solucionar
      EnviarColores(); //Asumiendo que se mande uno por uno
      MoverMotor(X, i, Derecha);
    }
    MoverMotor(X, 4, Izquierda); //Volver a posición inicial para la siguienteFila
  }
  SubirPiston();
  MoverMotor(Y, 4, Arriba);
}

void ConfigurarIman(int Pin){
  PinIman = Pin;
}

void ApagarIman(){
  digitalWrite(PinIman, 0);
}

void EncenderIman(){
  digitalWrite(PinIman, 1);
}

void ConfigurarPiston(){

}

void SubirPiston(){

}

void BajarPiston(){

}

void ParenTodo(){

}