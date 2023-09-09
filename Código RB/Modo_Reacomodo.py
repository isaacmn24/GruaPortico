#Codigo de reacomodo
#Para el funcionamiento correcto se debe mantener el mismo orden de la grid_espacial

#array para la posición de los colores escaneados en la matriz espacial
Color_Rojo = []
Color_Azul = []
Color_Amarillo = []
Color_Blanco = []

#Array para la posición de los colores correcta en la matriz espacial
C_Rojo = []
C_Azul = []
C_Amarillo = []
C_Blanco = []

#Array Movimientos a realizar
Movimientos_grua = [[5,5]]


#Matriz de la posición en el espacio 5x5
grid_espacial = [[[0,0], [1,0], [2,0], [3,0], [4,0]],
                 [[0,1], [1,1], [2,1], [3,1], [4,1]],
                 [[0,2], [1,2], [2,2], [3,2], [4,2]],
                 [[0,3], [1,3], [2,3], [3,3], [4,3]],
                 [[0,4], [1,4], [2,4], [3,4], [4,4]]]

#Colores:
#Rojo = 1
#Azul = 2
#Amarillo = 3
#Blanco o Vacío = 4


#Archivo excel donde viene la posición de los objetos correctamente
matriz_correcta = [[1, 2, 3, 1, 3],
                   [2, 1, 1, 2, 2],
                   [1, 2, 3, 2, 3],
                   [1, 2, 3, 1, 2],
                   [3, 2, 3, 1, 3]]
# 8 color rojo
# 9 color azul
# 8 color amarillo


#Esta matriz se consigue escaneando la matriz 5x5
matriz_escaneada = [[3, 2, 1, 1, 3],
                    [2, 1, 1, 3, 1],
                    [1, 1, 3, 2, 3],
                    [1, 2, 3, 2, 4],
                    [2, 2, 2, 3, 3]]
# 8 color rojo
# 8 color azul
# 8 color amarillo
# 1 color blanco


#Orden ascendente de la posicion en la matriz para los distintos objetos de la matriz con los objetos ordenados correctamente
def leer_matriz_correcta(M,R,A,Y,B):
    filas = len(M)
    columnas = len(M[0])
    for i in range(filas):
        for j in range(columnas):
            if M[j][i] == 1:
                R.append(grid_espacial[j][i])
            elif M[j][i] == 2:
                A.append(grid_espacial[j][i])
            elif M[j][i] == 3:
                Y.append(grid_espacial[j][i])
            elif M[j][i] == 4:
                B.append(grid_espacial[j][i])        


#Orden descendente de la posicion en la matriz para los distintos objetos escaneados
def leer_matriz_escaneada(M,R,A,Y,B):
    filas = len(M)
    columnas = len(M[0])
    for i in range(filas-1,-1,-1):
        for j in range(columnas-1,-1,-1):
            if M[j][i] == 1:
                R.append(grid_espacial[j][i])
            elif M[j][i] == 2:
                A.append(grid_espacial[j][i])
            elif M[j][i] == 3:
                Y.append(grid_espacial[j][i])
            elif M[j][i] == 4:
                B.append(grid_espacial[j][i])        
            

#Va agregando a un array la sucesión de posiciones para colocar los objetos
def lista_de_movimientos(CR,R,CA,A,CY,Y,CB,B):
    posicion = obtener_posicion(CR,CA,CY,CB)
    contador_rojo = 0
    contador_azul = 0
    contador_amarillo = 0
    contador_blanco = 0
    posicion_inicial = []
    if posicion == 1:
        Movimientos_grua.append(CR[0])
        posicion_inicial.append(R[0])
        contador_rojo = contador_rojo + 1
    elif posicion == 2:
        Movimientos_grua.append(CA[0])
        posicion_inicial.append(A[0])
        contador_azul = contador_azul + 1
    elif posicion == 3:
        Movimientos_grua.append(CY[0])
        posicion_inicial.append(Y[0])
        contador_amarillo = contador_amarillo + 1
    elif posicion == 4:
        Movimientos_grua.append(CB[0])
        posicion_inicial.append(B[0])
        contador_blanco = contador_blanco + 1
        
    Movimientos_grua.append(posicion_inicial[0])   
    while Movimientos_grua[1] != posicion_inicial[0]:
        Macolor = obtiene_Mcolor(posicion_inicial)
        if Macolor == 1:
            posicion_inicial[0] = R[contador_rojo]
            Movimientos_grua.append(posicion_inicial[0])
            contador_rojo = contador_rojo + 1
        elif Macolor == 2:
            posicion_inicial[0] = A[contador_azul]
            Movimientos_grua.append(posicion_inicial[0])
            contador_azul = contador_azul + 1
        elif Macolor == 3:
            posicion_inicial[0] = Y[contador_amarillo]
            Movimientos_grua.append(posicion_inicial[0])
            contador_amarillo = contador_amarillo + 1
        elif Macolor == 4:
            posicion_inicial[0] = B[contador_blanco]
            contador_blanco = contador_blanco + 1
    Movimientos_grua[(len(Movimientos_grua))-1] = Movimientos_grua[0]

#Obtiene a cual posicion se debe colocar el objeto
def obtiene_Mcolor(Xi):
    Mcolor = 0
    for i in range(len(C_Rojo)):
        if Xi[0] == C_Rojo[i]:
            Mcolor = 1
            return Mcolor
    for j in range(len(C_Azul)):
        if Xi[0] == C_Azul[j]:
            Mcolor = 2
            return Mcolor
    for y in range(len(C_Amarillo)):
        if Xi[0] == C_Amarillo[y]:
            Mcolor = 3
            return Mcolor
    for k in range(len(C_Rojo)):
        if Xi[0] == C_Blanco[k]:
            Mcolor = 4
            return Mcolor
   

#Obtiene la posición donde se encuentra el objeto
def obtener_posicion(CR,CA,CY,CB):
    a = len(CR)
    b = len(CA)
    c = len(CY)
    d = len(CB)
    posicion = 0
    if a != 0:
        posicion = 1
        return posicion
    elif b != 0:
        posicion = 2
        return posicion
    elif c != 0:
        posicion = 3
        return posicion
    elif d != 0:
        posicion = 4
        return posicion
    

#va descartando los valores que se encuentran correctamente
#busca los indices de los valores correctosd entre la amtriz correcta y la matriz escaneada y llama borrar_valor
def eliminar_valor(CC,CE):
    filas_correctas = len(CC)
    indice_correcto = []
    indice_escaneado = []
    for i in range(filas_correctas):
        filas_escaneadas = len(CE)
        for j in range(filas_escaneadas):
            if CC[i] == CE[j]: 
                indice_correcto.append(i)
                indice_escaneado.append(j)
    borrar_correcto(CC,indice_correcto)
    borrar_escaneado(CE,indice_escaneado)


#borra los valores del array que se repiten (matriz correcta)
def borrar_correcto(M,indice):
    for x in range(len(indice)-1,-1,-1):
        del M[indice[x]]


#borra los valores del array que se repiten (matriz escaneada)
def borrar_escaneado(M,indice):
    for x in range(len(indice)):
        del M[indice[x]]



#Esta funcion es para ir viendo los valores en los array
def matriz_color(P):
    fila = len(P)
    for i in range(fila):
        print("| {0} ".format(P[i]), sep=',', end='')
        print('|')


#Función que recibe la posición del objeto mal colocado y la posición a la que debe cambiarlo
#Programación que le llega los movimientos a realizar y los implementa fisicamente
def mover_objeto(M_movimientos):
    i = 0
    num = len(M_movimientos) - 1
    print("---------------------------------------------\n")
    while i < num:
        print("El valor inicial es (mover objeto) ",M_movimientos[i+1],"\n")
        print("El valor final es (colocar objeto) ",M_movimientos[i],"\n")
        print("---------------------------------------------\n")
        i = i + 1


#Llamar Modo Reacomodo
def Modo_Reacomodo():
    leer_matriz_correcta(matriz_correcta,C_Rojo,C_Azul,C_Amarillo,C_Blanco)
    leer_matriz_escaneada(matriz_escaneada,Color_Rojo,Color_Azul,Color_Amarillo,Color_Blanco)
    eliminar_valor(C_Rojo,Color_Rojo)
    eliminar_valor(C_Azul,Color_Azul)
    eliminar_valor(C_Amarillo,Color_Amarillo)
    eliminar_valor(C_Blanco,Color_Blanco)
    lista_de_movimientos(C_Rojo,Color_Rojo,C_Azul,Color_Azul,C_Amarillo,Color_Amarillo,C_Blanco,Color_Blanco)
    mover_objeto(Movimientos_grua)
