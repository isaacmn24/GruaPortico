class Motor:
    # Esta clase sirve para almacenar la información de los motores como la posición general
    # También envía las instrucciones al arduino para mover los motores a través del protocolo
    
    def __init__(self, pos):
        self.pos = [0,0]
        self.objetos = []
    
    def posicion(self):
        return self.pos
    
    def mover(self, posicion):
        movimientoX = self.pos[0] - posicion[0]
        movimientoY = self.pos[1] - posicion[1]
        
        # Aqui se codifica los movimientos en una serie de bits que se envía al arduino
        # La idea es tener una codificación interna clara para determinar si el movimiento
        # es a la izquierda (positivo) o a la derecha (negativo) y cuántas unidades
        
        # Queda pendiente hacer la interfaz arduino - RB
        
        self.pos = posicion
        return 
      
    def barrer(self):
        # Este método barre toda la cuadrícula. 
        # Si el arduino encuentra un objeto suena la alarma y envía una señal a la RB
        # Al recibir la señal se guarda la posición en la que se detectó el objeto
        
        self.pos = [0,0]
        
        # MOVER A POS
        
        #Empezar a barrer
        for i in range(6):  # 6 equivale a filas-1
            for j in range(6):
                
                # MOVER A [i,j]
                
                # IF ALARMA
                # pos_objeto = [i,j]
                # self.objetos.append(pos_objeto)
                
        