# Funciones para leer salidas de modos de acomodo y demás
import Modo_Reacomodo_y_Patron
modo_op, M_movimientos, M_escaneada, M_correcta, M_master = Modo_Reacomodo_y_Patron.Modo_Reacomodo()
# modo_op me indica si el modo es con o sin espacios vacios
    # Función que busca cada coordenada de moviemiento, inicio y fin,
    # de forma que se realice el recorrido secuencialmente en interfaz.
def movimientos(c_recorrido):
    Recorrido = c_recorrido
    coordenadas_i = M_movimientos[Recorrido+1]
    coordenadas_f = M_movimientos[Recorrido]
    for i in range (len(M_master)): 
        coordenada_escaneada = [M_master[i][0],M_master[i][1]]
        if coordenadas_i == coordenada_escaneada:
            color = M_master[i][2]
            
    return coordenadas_i, coordenadas_f, color

def llamar_movimientos(Input_recorrido):
    recorrido = Input_recorrido
    coordenadas_i, coordenadas_f, color = movimientos(recorrido)
    return modo_op,M_movimientos, M_master, coordenadas_i, coordenadas_f, color

