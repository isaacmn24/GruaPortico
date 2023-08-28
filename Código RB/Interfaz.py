import pygame, sys
import random

rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
 
diccionario = {0:rojo, 1:verde, 2:azul}

matriz=[]

eliminar=0

pygame.init()

# Tamaño de Pantalla
pantalla_X = 900
pantalla_Y = 600

# Ubicación y tamaño de círculo
Circulo_X = 60
Circulo_Y = 300
Objetivo_X = -1
Objetivo_Y = 3

# Espaciado matriz
eje_x = 210
eje_y = 50

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

				Circulo_X = 55 # Coloco el nuevo
				Circulo_Y = 300

				Objetivo_X = -1
				Objetivo_Y = 3

				color = random.randint(0,2)

			if event.key == pygame.K_e: # Si presiono e
			
				del matriz[0]


	ventana.fill((255,255,255)) # Fondo blanco


	# Matriz
	for i in range (6):
		pygame.draw.line(ventana, rojo, [eje_x+(100*(i)),eje_y], [eje_x+(100*(i)),eje_y+500],4) # verticales
		pygame.draw.line(ventana, rojo, [eje_x,eje_y+(100*i)], [eje_x+500,eje_y+(100*i)],4) # horizontales

	# Cuadro de carga
	pygame.draw.line(ventana, rojo, [10,250], [10, 350],4)
	pygame.draw.line(ventana, rojo, [110,250], [110, 350],4)
	pygame.draw.line(ventana, rojo, [10,250], [110,250],4)
	pygame.draw.line(ventana, rojo, [10,350], [110,350],4)

	# ########################
	Destino_X = (Objetivo_X*100)+(160) # Expresion matemática para moverse entre centros (no pregunten como la saqué)
	Destino_Y = (Objetivo_Y*100)
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
		pygame.draw.circle(ventana,diccionario[matriz[i][2]], (((matriz[i][0]*100)+(160)),((matriz[i][1]*100))), 30)

	pygame.display.flip() # Refrescar pantalla
	reloj.tick(60) # FPS
