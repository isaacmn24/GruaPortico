import serial 

# ser = serial.Serial("/dev/ttyACM0", 9600)   # Serial port on Raspberry Pi

def recibirColores():
    """
    Descripción
    -------
    Para que esta función se concrete tendrá que pasar por cada
    uno de los 25 espacios y recibir un dato del STM32, si no recibe
    nada, no avanzará y se quedará enfrascada esperando por siempre.
    
    Returns
    -------
    Retorna la matriz escaneada por el STM32

    """
    print("datos")
    matriz_escaneada = [[3, 1, 4, 4, 4],
                        [3, 2, 2, 2, 1],
                        [3, 4, 1, 3, 1],
                        [1, 2, 4, 1, 4],
                        [4, 1, 2, 3, 4]]
    # for fila in matriz_escaneada:
    #     for columna in fila:
    #         while ser.in_waiting <= 0:
    #             if ser.in_waiting() > 0:
    #                 color = ser.read(1)
    #                 matriz_escaneada[fila][columna] = color
    return matriz_escaneada


def enviarSTM32(dato):
    """
    Parametros
    ----------
    dato : BYTE
        Dato a enviar al STM32.

    Returns
    -------
    Retorna un 1 si se envió satisfactoriamente el dato.

    """
    # return ser.write(dato)

def recibirSTM32():
    """
    Retorna el byte leído de la STM32
    """
    print("dato")
    # while ser.in_waiting <= 0:
    #     if ser.in_waiting() > 0:
    #         return ser.read(1)