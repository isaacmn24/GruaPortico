/*
  Este código controla todos los sensores presentes en la grúa:
  1. HCSR-04 se encarga de medir distancia. Se utiliza en el protocolo de inicio
    para detectar si hay obstáculos en el camino.
    Utiliza dos pines digitales: PB0 y PB1.
  2. ISL29125 se encarga de medir colores. Se utiliza para detectar el tipo de bloque.
    Utiliza comunicación por I2C. Utiliza el primer canal (PB6 y PB7)

  Aqui no se hace comunicación con el Raspberry pi, solamente se mide el sensor solicitado.
*/

// LIBRERÍAS
//#include <Wire.h>
#include <SparkFunISL29125.h>
#include <HCSR04.h>

// GPIO; UTILIZAR DEFINE
#define triggerPin PB1
#define echoPin PB0

// SENSOR DE COLOR
SFE_ISL29125 RGB_sensor;


void setup_sensores()
{
  // INICIO SENSORES
  // ****** Idea: Hacer función que compruebe funcionamiento de sensores, para que si no funciona alguno de los dos lo avise
  HCSR04.begin(triggerPin, echoPin);
  if (RGB_sensor.init())
  {
    Serial.println("Sensor Initialization Successful\n\r");
  }
}

unsigned int *leerColores()
{
  static unsigned int rgb[3];   // Array que contiene los valores RGB leídos por el sensor
  rgb[0] = RGB_sensor.readRed();    // Leer rojo
  rgb[1] = RGB_sensor.readGreen();  // Leer verde
  rgb[2] = RGB_sensor.readBlue();   // Leer azul
  return rgb;
}

double leerDistancia()
{
  double* distancias = HCSR04.measureDistanceCm();
  return distancias[0];
}

