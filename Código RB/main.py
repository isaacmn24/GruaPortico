import Modo_Reacomodo

M_movimientos=Modo_Reacomodo.Modo_Reacomodo()

def mover_objeto(M_movimientos):
    i = 0
    num = len(M_movimientos) - 1
    print("---------------------------------------------\n")
    while i < num:
        print("El valor inicial es (mover objeto) ",M_movimientos[i+1],"\n")
        print("El valor final es (colocar objeto) ",M_movimientos[i],"\n")
        print("---------------------------------------------\n")
        i = i + 1

mover_objeto(M_movimientos)