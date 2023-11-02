
import pygame
import sys
from Interfaz import Pantalla
import Modo_Reacomodo_y_Patron
import Funciones_recorrido_acomodo

 
def main():
    pygame.init()
    # Tamaño de Pantalla m
    pantalla_X = 900
    pantalla_Y = 600

    # creacion de objeto pantalla
    pantalla = Pantalla(pantalla_X,pantalla_Y)
    reloj = pygame.time.Clock()

    # Ejecuta la interfas y le ingresa todos los datos de ubicacíon y traslado
    pantalla.pre_ejecucion()
          
 
if __name__ == "__main__":
    main()
