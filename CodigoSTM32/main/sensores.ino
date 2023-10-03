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
#include <Wire.h>
#include <SparkFunISL29125.h>
#include <HCSR04.h>

// GPIO; UTILIZAR DEFINE
#define triggerPin PB1
#define echoPin PB0

// SENSOR DE COLOR
SFE_ISL29125 RGB_sensor;
<<<<<<< HEAD
=======
UltraSonicDistanceSensor ultrasonic_sensor(triggerPin, echoPin);  // Initialize sensor that uses digital pins 13 and 12.
>>>>>>> ea1679d1b09f9b56a775a4cd2e5ab226f187f2fe

void setup_sensores()
{
  // INICIO SENSORES
  // ****** Idea: Hacer función que compruebe funcionamiento de sensores, para que si no funciona alguno de los dos lo avise
  if (RGB_sensor.init())
  {
    Serial.println("Sensor Initialization Successful\n\r");
  }
}

<<<<<<< HEAD
unsigned int leerColores(unsigned int *rgb)
{
  // Array que contiene los valores RGB leídos por el sensor
=======
void leerColores(unsigned int *rgb)
{
>>>>>>> ea1679d1b09f9b56a775a4cd2e5ab226f187f2fe
  rgb[0] = RGB_sensor.readRed();    // Leer rojo
  rgb[1] = RGB_sensor.readGreen();  // Leer verde
  rgb[2] = RGB_sensor.readBlue();   // Leer azul
}

float leerDistancia()
{
  return ultrasonic_sensor.measureDistanceCm();
}

