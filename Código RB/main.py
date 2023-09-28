# import Modo_Reacomodo
import pygame
import sys
from Interfaz import Pantalla

def main():
    pygame.init()
    # Tamaño de Pantalla
    pantalla_X = 900
    pantalla_Y = 600

    # creacion de objeto pantalla
    pantalla = Pantalla(pantalla_X,pantalla_Y)
    reloj = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pantalla.ejecutar(5,5)
        
        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    main()

# # # Tamaño de Pantalla
# # pantalla_X = 900
# # pantalla_Y = 600

# # # creacion de objeto pantalla
# # pantalla = Pantalla(pantalla_X,pantalla_Y)

# # while True:
# #     #manda constantemente coordenada y ejecuta pantalla
# #     pantalla.ejecutar(4,4)
# M_movimientos=Modo_Reacomodo.Modo_Reacomodo()

# def mover_objeto(M_movimientos):
#     i = 0
#     num = len(M_movimientos) - 1
#     print("---------------------------------------------\n")
#     while i < num:
#         print("El valor inicial es (mover objeto) ",M_movimientos[i+1],"\n")
#         print("El valor final es (colocar objeto) ",M_movimientos[i],"\n")
#         print("---------------------------------------------\n")
#         i = i + 1

# mover_objeto(M_movimientos)