# Funciones para leer salidas de modos de acomodo y demás
import Modo_Reacomodo_y_Patron

# modo_op, M_movimientos, M_escaneada, M_correcta, M_master = Modo_Reacomodo_y_Patron.Modo_Reacomodo()
# modo_op me indica si el modo es con o sin espacios vacios
    # Función que busca cada coordenada de moviemiento, inicio y fin,
    # de forma que se realice el recorrido secuencialmente en interfaz.
def movimientos(c_recorrido, modo_op, M_movimientos, M_master):
    if modo_op == 'Modo Patron':
        Recorrido = c_recorrido
        coordenadas_i = M_movimientos[Recorrido+1]
        coordenadas_f = M_movimientos[Recorrido]
        for i in range (len(M_master)): 
            coordenada_escaneada = [M_master[i][0],M_master[i][1]]
            if coordenadas_f == coordenada_escaneada: # Para que funcione modo patrón
                color = M_master[i][2]

###    que en modo parón no aparesca la matriz y que si se vaya creando
    else:
        Recorrido = c_recorrido
        coordenadas_i = M_movimientos[Recorrido+1]
        coordenadas_f = M_movimientos[Recorrido]
        for i in range (len(M_master)): 
            coordenada_escaneada = [M_master[i][0],M_master[i][1]]
            if coordenadas_i == coordenada_escaneada: # Para modo reacomodo
                color = M_master[i][2]
                M_master[i][2] = 4 # Solo para Modo Reacomodo

    return coordenadas_i, coordenadas_f, color


def llamar_movimientos(Input_recorrido, modo_op, M_movimientos, M_escaneada, M_correcta, M_master):
    recorrido = Input_recorrido
    coordenadas_i, coordenadas_f, color = movimientos(recorrido, modo_op, M_movimientos, M_master)
    return M_movimientos, M_master, coordenadas_i, coordenadas_f, color

#  nueva función que se ejecute cuandose oprima un botón y con esto se recoelcten los datos, y se envien al modo para que empiece el recorrido, modo reacomodo