import pygame
import sys
import pyautogui
import Funciones_recorrido_acomodo
import Modo_Reacomodo_y_Patron
import comunicacion

reloj = pygame.time.Clock()

rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
blanco = (255, 255, 255)

diccionario = {1: rojo, 2: azul, 3: verde, 4: blanco}

Boton_ancho = 50
Boton_largo = 220


# Clase para creación de pantalla y poder ingresarle datos desde main
class Pantalla(object):
    def __init__(self, Pantalla_X, Pantalla_Y):
        pygame.init()

        pygame.display.set_caption("Grúa Pórtico")

        self.pantalla_X = Pantalla_X
        self.pantalla_Y = Pantalla_Y
        self.resolucion = (self.pantalla_X, self.pantalla_Y)

        self.ventana = pygame.display.set_mode(self.resolucion)

        self.matriz = []

        self.M_recorrido = 0

        self.Inicio = 0
        self.boton_m_patron = None
        self.boton_m_reacomodo = None

    # Función que dibuja los elementos en pantalla
    def dibujar_pantalla(self):
        self.ventana.fill((204, 204, 204))  # Fondo blanco

        # Espaciado matriz
        eje_x = 210
        eje_y = 50

        # Matriz
        for i in range(6):
            pygame.draw.line(self.ventana, rojo, [eje_x + (100 * (i)), eje_y], [eje_x + (100 * (i)), eje_y + 500], 4)
            pygame.draw.line(self.ventana, rojo, [eje_x, eje_y + (100 * i)], [eje_x + 500, eje_y + (100 * i)], 4)

        # Cuadro de carga
        pygame.draw.line(self.ventana, rojo, [10, 250], [10, 350], 4)
        pygame.draw.line(self.ventana, rojo, [110, 250], [110, 350], 4)
        pygame.draw.line(self.ventana, rojo, [10, 250], [110, 250], 4)
        pygame.draw.line(self.ventana, rojo, [10, 350], [110, 350], 4)

        for i in range(len(self.matriz)):
            pygame.draw.circle(self.ventana, diccionario[self.matriz[i][2]],
                               (((self.matriz[i][0] * 100) + (160)), ((self.matriz[i][1] * 100))), 30)

        if 'pieza' in globals():
            pieza.draw(self.ventana)

        # Dibujar botones
        self.boton_m_patron.definir(self.ventana)
        self.boton_m_patron.textoboton(self.ventana)

        self.boton_m_reacomodo.definir(self.ventana)
        self.boton_m_reacomodo.textoboton(self.ventana)

        pygame.display.flip()

    def ejecutar(self):
        global pieza

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        modo_op, Movs, M_escaneada, M_correcta, M_master = Modo_Reacomodo_y_Patron.Modo_Patron()
                        print(modo_op)
                    if event.key == pygame.K_o:
                        modo_op, Movs, M_escaneada, M_correcta, M_master = Modo_Reacomodo_y_Patron.Modo_Reacomodo()
                        print(modo_op)
                    if event.key == pygame.K_i:
                        M_movimientos, M_Master_mod, coordenadas_i, coordenadas_f, color = \
                            Funciones_recorrido_acomodo.llamar_movimientos(self.M_recorrido, modo_op, Movs,
                                                                          M_escaneada, M_correcta, M_master)
                        self.Inicio = 1

                        Objetivo_X = coordenadas_i[0]
                        Objetivo_Y = coordenadas_i[1]
                        Circulo_X = (Objetivo_X * 100) + (160)
                        Circulo_Y = (Objetivo_Y * 100)
                        Color = color

                        pieza = Circulo(Circulo_X, Circulo_Y, Color, Objetivo_X, Objetivo_Y)

                        self.Direcion_X = coordenadas_f[0]
                        self.Direcion_Y = coordenadas_f[1]

                        if modo_op == 'Modo Patron':
                            self.matriz = self.matriz
                        else:
                            self.matriz = M_Master_mod

                    if event.key == pygame.K_m:
                        pieza.Objetivo_X = self.Direcion_X
                        pieza.Objetivo_Y = self.Direcion_Y

                    if event.key == pygame.K_SPACE:
                        self.matriz.append([pieza.Objetivo_X, pieza.Objetivo_Y, pieza.Color])
                        self.M_recorrido = self.M_recorrido + 1

                        if modo_op == 'conesp' or modo_op == 'Modo Patron':
                            self.M_recorrido = self.M_recorrido + 1

                        if (self.M_recorrido) < (len(M_movimientos) - 1):
                            movs, M_Master_mod, coordenadas_i, coordenadas_f, color = \
                                Funciones_recorrido_acomodo.llamar_movimientos(self.M_recorrido, modo_op, Movs,
                                                                              M_escaneada, M_correcta, M_master)

                            Objetivo_X = coordenadas_i[0]
                            Objetivo_Y = coordenadas_i[1]
                            Circulo_X = (Objetivo_X * 100) + (160)
                            Circulo_Y = (Objetivo_Y * 100)
                            Color = color

                            pieza = Circulo(Circulo_X, Circulo_Y, Color, Objetivo_X, Objetivo_Y)

                            self.Direcion_X = coordenadas_f[0]
                            self.Direcion_Y = coordenadas_f[1]

                            if modo_op == 'Modo Patron':
                                self.matriz = self.matriz
                            else:
                                self.matriz = M_Master_mod
                        else:
                            pyautogui.alert("Fin Reacomodo")

                    if event.key == pygame.K_e:
                        self.matriz = []

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (755 <= mouse[0] <= 970) and (50 <= mouse[1] <= 100):
                        pygame.quit()
                self.boton_m_patron.verificar_clic(event)
                self.boton_m_reacomodo.verificar_clic(event)

            self.dibujar_pantalla()
            mouse = pygame.mouse.get_pos()
            
            if 'pieza' in globals():
                pieza.Posicionamiento()

            reloj.tick(60)


    def pre_ejecucion(self):
        coor_x = 755
        coor_y = 50
        self.boton_m_patron = Boton(coor_x, coor_y + 80, Boton_largo, Boton_ancho, "Modo Patron")
        self.boton_m_reacomodo = Boton(coor_x, coor_y + 160, Boton_largo, Boton_ancho, "Modo Reacomodo")

        self.ejecutar()


# Clase para objeto que se va a mover
class Circulo(object):
    def __init__(self, Circulo_X, Circulo_Y, Color, Objetivo_X, Objetivo_Y):
        self.Circulo_X = Circulo_X
        self.Circulo_Y = Circulo_Y
        self.Objetivo_X = Objetivo_X
        self.Objetivo_Y = Objetivo_Y
        self.Color = Color

    def draw(self, ventana):
        pygame.draw.circle(ventana, diccionario[self.Color], (self.Circulo_X, self.Circulo_Y), 30)

    def Posicionamiento(self):
        Destino_X = (self.Objetivo_X * 100) + (160)
        Destino_Y = (self.Objetivo_Y * 100)

        if self.Circulo_X > Destino_X:
            self.Circulo_X -= 5

        if self.Circulo_X < Destino_X:
            self.Circulo_X += 5

        if self.Circulo_Y > Destino_Y:
            self.Circulo_Y -= 5

        if self.Circulo_Y < Destino_Y:
            self.Circulo_Y += 5


# Clase para objeto que se va a mover
class Boton(object):
    def __init__(self, button_x_, button_y_, Boton_largo, Boton_ancho, label):
        self.button_x_ = button_x_
        self.button_y_ = button_y_
        self.Boton_largo = Boton_largo
        self.Boton_ancho = Boton_ancho
        self.label = label
        self.boton_m = None

    def definir(self, ventana):
        button_color = (171, 171, 171)
        self.boton_m = pygame.Rect(self.button_x_, self.button_y_, self.Boton_largo, self.Boton_ancho)
        pygame.draw.rect(ventana, button_color, self.boton_m)

    def textoboton(self, ventana):
        font = pygame.font.Font(None, 30)
        text = font.render(self.label, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.boton_m.center)
        ventana.blit(text, text_rect)

    def verificar_clic(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.boton_m.collidepoint(mouse_pos):
                if self.label == "Modo Patron":
                    comunicacion.recibirSTM32()
                else:
                    Matriz_de_lectura = comunicacion.recibirColores()
                    Modo_Reacomodo_y_Patron.matriz_escaneda_lectura(Matriz_de_lectura)
                    
                    