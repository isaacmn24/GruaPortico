/*
  Este código controla todos los sensores presentes en la grúa:
  1. HCSR-04 se encarga de medir distancia. Se utiliza en el protocolo de inicio
    para detectar si hay obstáculos en el camino.
    Utiliza dos pines digitales: PB0 y PB1.
  2. TCS3200 se encarga de medir colores. Se utiliza para detectar el tipo de bloque.
   )

  Aqui no se hace comunicación con el Raspberry pi, solamente se mide el sensor solicitado.
*/
// LIBRERÍAS
#include <HCSR04.h>

// GPIO; UTILIZAR DEFINE
#define triggerPin PB1
#define echoPin PB0
#define sensorColor_S2 PB12
#define sensorColor_S3 PB13
#define sensorColor_salida PB14

// GUARDAR FRECUENCIAS Y VALORES RGB
int frecuenciaRojo = 0;
int frecuenciaVerde = 0;
int frecuenciaAzul = 0;
int colorRojo;
int colorVerde;
int colorAzul;

void setup() {
  // Definiendo las Salidas
  pinMode(sensorColor_S2, OUTPUT);
  pinMode(sensorColor_S3, OUTPUT);
  
  // Definiendo salidaSensor como entrada
  pinMode(sensorColor_salida, INPUT);

  // Sensor ultrasónico
  HCSR04.begin(triggerPin, echoPin);

  // Monitor serial para ver los valores de los colores
  Serial.begin(115200);
}

void loop()
{
  // Definiendo la lectura de los fotodiodos con filtro rojo
  digitalWrite(sensorColor_S2,LOW);
  digitalWrite(sensorColor_S3,LOW);
  
  // Leyendo la frecuencia de salida del sensor
  frecuenciaRojo = pulseIn(sensorColor_salida, LOW);
  
  // Mostrando por el monitor Serial el valor para el rojo (R = Red)
  Serial.print("R = ");
  Serial.print(frecuenciaRojo);
  delay(100);
  
  // Definiendo la lectura de los fotodiodos con filtro verde
  digitalWrite(sensorColor_S2,HIGH);
  digitalWrite(sensorColor_S3,HIGH);
  
  // Leyendo la frecuencia de salida del sensor
  frecuenciaVerde = pulseIn(sensorColor_salida, LOW);

  // Mostrando por el monitor Serial el valor para el verde (G = Green)
  Serial.print(" G = ");
  Serial.print(frecuenciaVerde);
  delay(100);
 
  // Definiendo la lectura de los fotodiodos con filtro azul
  digitalWrite(sensorColor_S2,LOW);
  digitalWrite(sensorColor_S3,HIGH);
  
  // Leyendo la frecuencia de salida del sensor
  frecuenciaAzul = pulseIn(sensorColor_salida, LOW);
  
  // Mostrando por el monitor Serial el valor para el azul (B = Blue)
  Serial.print(" B = ");
  Serial.println(frecuenciaAzul);
  delay(100);

  // Comprobar cual es el color detectado y mostrarlo
  // esta parte del código realmente va en la RASP
  // int color;
  // if(colorRojo > colorVerde && colorRojo > colorAzul){        // Color rojo
  //   color = 1;
  // }
  // else if(colorVerde > colorRojo && colorVerde > colorAzul){  // Color verde
  //   color = 3;
  // }
  // else if(colorAzul > colorRojo && colorAzul > colorVerde){   // Color azul
  //   color = 2;
  // }
  // else {                                                      // Espacio vacío
  //   color = 4;
  // }
}

bool alarmaDistancia()
{
  if (HCSR04.measureDistanceCm()[0] < 20){
    return 1;
  }
  else{
    return 0;
  }
}


