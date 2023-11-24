// LIBRERÍAS
//#include "sensores.h"
//#include "comunicacion.h"

// GPIO
#define pinDirMotores PA2
#define pinMotorX PA3
#define pinMotorY PA4
#define pinActuador PA4
#define pinIman PA6
#define pinCalibrarX PB4
#define pinCalibrarY PB5

// CONSTANTES DEL MOTOR
int PulRev = 6400;    // Pulsos por revolución
int Vel = 50;         // DelayMicroseconds - 50 funciona "bien"
int Distancia = 0;    // Distancia en cm entre las casillas de elementos
float RelRevTras = 0; // 1 revolución = ? cm lineales

//Para mover motores
bool X, Derecha, Abajo = 1; //No se si será así, hay que probar en planta
bool Y, Izquierda, Arriba = 0;

void CalibrarCero(){
  digitalWrite(pinDirMotores, 0); //Izquierda y arriba
  while(digitalRead(pinCalibrarX) == 0){
    digitalWrite(pinMotorX, HIGH); 
    delayMicroseconds(Vel); 
    digitalWrite(pinMotorX, LOW); 
    delayMicroseconds(Vel);
  }
  while(digitalRead(pinCalibrarY) == 0){
    digitalWrite(pinMotorY, HIGH); 
    delayMicroseconds(Vel); 
    digitalWrite(pinMotorY, LOW); 
    delayMicroseconds(Vel);
  }
}

void MoverMotor(int Motor, int Nivel, bool Direccion){
  float cantRev = Nivel*Distancia/RelRevTras;
  int cantPulsos = cantRev*PulRev;

  int Tipo;         //Definimos que motor mover
  if (Motor == 1){
    Tipo = pinMotorX;
  }
  else {
    Tipo = pinMotorY;
  }

  digitalWrite(pinDirMotores, Direccion); // Enables the motor to move in a particular direction
  for(int x = 0; x < cantPulsos; x++) {
    digitalWrite(Tipo, HIGH); 
    delayMicroseconds(Vel); 
    digitalWrite(Tipo, LOW); 
    delayMicroseconds(Vel); 
  }

}

void ApagarIman(){
  digitalWrite(pinIman, 0);
}

void EncenderIman(){
  digitalWrite(pinIman, 1);
}

void ConfigurarPiston(){

}

void SubirPiston(){

}

void BajarPiston(){

}

void ParenTodo(){

}

void EscaneoGeneral(){ //Asumiendo inicio en esquina superior izquierda
  BajarPiston();
  for (int u = 0; u <= 4; u++){
    MoverMotor(Y, u, Abajo);
    for (int i = 0; i <= 4; i++){

      if (alarmaDistancia()){
        ParenTodo();
      }

      int color = leerColores(); //cuanto tiempo debe estar aquí? un delay no lo va a solucionar
      EnviarColor(color); //Asumiendo que se mande uno por uno
      MoverMotor(X, i, Derecha);
    }
    MoverMotor(X, 4, Izquierda); //Volver a posición inicial para la siguienteFila
  }
  SubirPiston();
  MoverMotor(Y, 4, Arriba);
}
