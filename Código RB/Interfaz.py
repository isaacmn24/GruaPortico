import pygame, sys
import random

rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
 
diccionario = {0:rojo, 1:verde, 2:azul}

matriz=[]

pygame.init()

pantalla_X = 900
pantalla_Y = 600

Circulo_X = 90
Circulo_Y = 50
Objetivo_X = 1
Objetivo_Y = 1

Par_ordenado = 0

color = random.randint(0,2) # color inicial

resolucion = (pantalla_X,pantalla_Y)
reloj = pygame.time.Clock()

ventana = pygame.display.set_mode(resolucion)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Cerrar ventana
			sys.exit()

		
		if event.type == pygame.KEYDOWN: # Si aprieto una tecla (K_1 = casilla 1 y así)

			if event.key == pygame.K_1:
				if Par_ordenado == 0: # Pensada para X
					Objetivo_X = 1
				else:				  # Pensada para Y (Cambian con tab)
					Objetivo_Y = 1

			if event.key == pygame.K_2:
				if Par_ordenado == 0:
					Objetivo_X = 2
				else:
					Objetivo_Y = 2

			if event.key == pygame.K_3:
				if Par_ordenado == 0:
					Objetivo_X = 3
				else:
					Objetivo_Y = 3

			if event.key == pygame.K_4:

				if Par_ordenado == 0:
					Objetivo_X = 4
				else:
					Objetivo_Y = 4

			if event.key == pygame.K_5:

				if Par_ordenado == 0:
					Objetivo_X = 5
				else:
					Objetivo_Y = 5

			if event.key == pygame.K_TAB: # Si aprieto TAB

				if Par_ordenado == 0: # Cambio de coordenada
					Par_ordenado = 1
				else:
					Par_ordenado = 0

			if event.key == pygame.K_SPACE: # Si coloco nuevo objeto

				matriz.append([Objetivo_X, Objetivo_Y, color]) # Meto sus datos en lista

				Circulo_X = 90 # Coloco el nuevo
				Circulo_Y = 50

				Objetivo_X = 1
				Objetivo_Y = 1

				color = random.randint(0,2)


	ventana.fill((255,255,255)) # Fondo blanco


	# Matriz
	for i in range (4):
		pygame.draw.line(ventana, rojo, (900*(i+1)/5, 0), ((500*(i+1)/5, 900))) # verticales
		pygame.draw.line(ventana, rojo, (0, 900*(i+1)/5), ((500, 900*(i+1)/5))) # horizontales

	########################
	Destino_X = 2*Objetivo_X*(500/10)-(500/10) # Expresion matemática para moverse entre centros (no pregunten como la saqué)
	Destino_Y = 2*Objetivo_Y*(900/10)-(900/10)
	########################		

	############ MOVIMIENTO HORIZONTAL
	if (Circulo_X > Destino_X): 
		Circulo_X -= 5 # Este es el movimiento como tal (el 5 es la "velocidad")

	if (Circulo_X < Destino_X):
		Circulo_X += 5

	############ MOVIMIENTO VERTICAL
	if (Circulo_Y > Destino_Y):
		Circulo_Y -= 5

	if (Circulo_Y < Destino_Y):
		Circulo_Y += 5

	pygame.draw.circle(ventana, diccionario[color], (Circulo_X, Circulo_Y), 30) # Dibujar circulo actual

	for i in range (len(matriz)): # Recorrer la matriz dibujando los circulos previos
		pygame.draw.circle(ventana,diccionario[matriz[i][2]], (2*matriz[i][0]*(pantalla_X/10)-(pantalla_X/10), 2*matriz[i][1]*(pantalla_Y/10)-(pantalla_Y/10)), 30)




	pygame.display.flip() # Refrescar pantalla
	reloj.tick(60) # FPS

