# Funciones para leer salidas de modos de acomodo y demás
import Modo_Reacomodo_y_Patron
M_movimientos, M_escaneada, M_correcta, M_master = Modo_Reacomodo_y_Patron.Modo_Reacomodo()

    # Función que busca cada coordenada de moviemiento, inicio y fin,
    # de forma que se realice el recorrido secuencialmente en interfaz.
def movimientos(m_movimientos,c_recorrido):
    
    M_movimientos = m_movimientos
    Recorrido = c_recorrido
    coordenadas_i = M_movimientos[Recorrido+1]
    coordenadas_f = M_movimientos[Recorrido]
    
    return coordenadas_i, coordenadas_f

def llamar_movimientos(Input_recorrido):
    recorrido = Input_recorrido
    coordenadas_i, coordenadas_f = movimientos(M_movimientos,recorrido)
    return M_movimientos, M_master, coordenadas_i, coordenadas_f

