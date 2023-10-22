#cambios para comprobar 2 branch
import pygame, sys
import Funciones_recorrido_acomodo

reloj = pygame.time.Clock()

rojo = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
blanco = (255,255,255)
 
diccionario = {1:rojo, 2:azul, 3:verde, 4:blanco}

#Clase para creación de pantalla y poder ingresarle datos desde main
class Pantalla(object):
	def __init__(self,Pantalla_X, Pantalla_Y):
		pygame.init()
		
		pygame.display.set_caption("Grúa Pórtico")
		
		self.pantalla_X = Pantalla_X
		self.pantalla_Y = Pantalla_Y
		self.resolucion = (self.pantalla_X,self.pantalla_Y)
		
		self.ventana = pygame.display.set_mode(self.resolucion)

		self.matriz = []

		self.M_recorrido = 0
	
	# Función que dibuja los elementos en pantalla
	def dibujar_pantalla(self):
		self.ventana.fill((204,204,204)) # Fondo blanco

		# Espaciado matriz
		eje_x = 210
		eje_y = 50

		# Matriz
		for i in range (6):
			pygame.draw.line(self.ventana, rojo, [eje_x+(100*(i)),eje_y], [eje_x+(100*(i)),eje_y+500],4) # verticales
			pygame.draw.line(self.ventana, rojo, [eje_x,eje_y+(100*i)], [eje_x+500,eje_y+(100*i)],4) # horizontales

		# Cuadro de carga
		pygame.draw.line(self.ventana, rojo, [10,250], [10, 350],4)
		pygame.draw.line(self.ventana, rojo, [110,250], [110, 350],4)
		pygame.draw.line(self.ventana, rojo, [10,250], [110,250],4)
		pygame.draw.line(self.ventana, rojo, [10,350], [110,350],4)

		# Dibuja Pieza
		pieza.draw(self.ventana)

		# Recorrer la matriz dibujando los circulos previos 
		for i in range (len(self.matriz)): 
			pygame.draw.circle(self.ventana,diccionario[self.matriz[i][2]], (((self.matriz[i][0]*100)+(160)),((self.matriz[i][1]*100))), 30)
		
		pygame.display.flip() # Refrescar pantalla
		

	def ejecutar(self,Posicion_X,Posicion_Y,Direccion_X,Direccion_Y,M_Master,M_movimientos):

		global pieza
		
		Objetivo_X = Posicion_X
		Objetivo_Y = Posicion_Y
		Circulo_X = (Objetivo_X*100)+(160)
		Circulo_Y = (Objetivo_Y*100)
		Color = 1

		pieza = Circulo(Circulo_X,Circulo_Y,Color,Objetivo_X,Objetivo_Y)

		# Direcciónes que se indican al ejecutar pantalla, ahi deben de ir los circulos
		self.Direcion_X = Direccion_X
		self.Direcion_Y = Direccion_Y
		self.matriz = M_Master	

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: # Cerrar ventana
					sys.exit()

				if event.type == pygame.KEYDOWN: # Si aprieto una tecla 

					# Asigna los valores objetivo para mover circuos
					if event.key == pygame.K_m:
						pieza.Objetivo_X = self.Direcion_X
						pieza.Objetivo_Y = self.Direcion_Y

					if event.key == pygame.K_SPACE: # Si coloco nuevo objeto

						self.matriz.append([pieza.Objetivo_X, pieza.Objetivo_Y, pieza.Color]) # Meto sus datos en lista
						self.M_recorrido = self.M_recorrido + 1
					
						
						if (self.M_recorrido) < (len(M_movimientos)-1):
							movs, matrix, coordenadas_i, coordenadas_f = Funciones_recorrido_acomodo.llamar_movimientos(self.M_recorrido)

							Objetivo_X = coordenadas_i[0]
							Objetivo_Y = coordenadas_i[1]
							Circulo_X = (Objetivo_X*100)+(160)
							Circulo_Y = (Objetivo_Y*100)
							Color = 1

							pieza = Circulo(Circulo_X,Circulo_Y,Color,Objetivo_X,Objetivo_Y)

							# Direcciónes que se indican al ejecutar pantalla, ahi deben de ir los circulos
							self.Direcion_X = coordenadas_f[0]
							self.Direcion_Y = coordenadas_f[1]
					
					if event.key == pygame.K_e: # Si presiono e
					
						self.matriz = []

			self.dibujar_pantalla()

			pieza.Posicionamiento()

			reloj.tick(60) # FPs

	def pre_ejecucion(self,):
		matriz_movimientos, Matrix, coordenadas_i, coordenadas_f = Funciones_recorrido_acomodo.llamar_movimientos(self.M_recorrido)
		M_master = Matrix
		self.ejecutar(coordenadas_i[0],coordenadas_i[1],coordenadas_f[0],coordenadas_f[1],M_master, matriz_movimientos)

# Clase para objeto que se va a mover
class Circulo(object):
	def __init__(self,Circulo_X,Circulo_Y,Color,Objetivo_X,Objetivo_Y):
		# Ubicación y tamaño de círculo
		self.Circulo_X = Circulo_X
		self.Circulo_Y = Circulo_Y
		self.Objetivo_X = Objetivo_X
		self.Objetivo_Y = Objetivo_Y
		self.Color = Color
	
	# Dibuja el circulo según posicionamiento
	def draw(self, ventana):
		# Dibujar circulo actual
		pygame.draw.circle(ventana, diccionario[self.Color], (self.Circulo_X, self.Circulo_Y), 30)

	# Ubica el circulo en el espacio
	def Posicionamiento(self):
		#########################
		Destino_X = (self.Objetivo_X*100)+(160) # Expresion matemática para moverse entre centros
		Destino_Y = (self.Objetivo_Y*100)
		########################		

		############ MOVIMIENTO HORIZONTAL
		if (self.Circulo_X > Destino_X): 
			self.Circulo_X -= 5 # Este es el movimiento como tal (el 5 es la "velocidad")

		if (self.Circulo_X < Destino_X):
			self.Circulo_X += 5

		############ MOVIMIENTO VERTICAL
		if (self.Circulo_Y > Destino_Y):
			self.Circulo_Y -= 5

		if (self.Circulo_Y < Destino_Y):
			self.Circulo_Y += 5


# # Ubicación y dirección de pieza
# Circulo_X = 60
# Circulo_Y = 300
# Objetivo_X = -1
# Objetivo_Y = 3
# Color = random.randint(1,3) # color inicial

# pieza = Circulo(Circulo_X,Circulo_Y,Color,Objetivo_X,Objetivo_Y)

# Quitar comentarios si se quiere probar

# # Tamaño de Pantalla
# pantalla_X = 900
# pantalla_Y = 600

# # creacion de objeto pantalla
# pantalla = Pantalla(pantalla_X,pantalla_Y)

# # Manda coordenada, que se asigna al presionar m
# pantalla.ejecutar(4,4)

# se sigue guardando con el espacio



