#import time
# Motor.py
import lectura_csv

#motor = Motor()

# Esta matriz contiene las coordenads del espacio físico
# Ahora es un espacio gigante, pero la idea es hacerlo tan preciso como queramos
# Se aceptan otras ideas más eficientes
grid_espacial = [[[0,5], [1,5], [2,5], [3,5], [4,5], [5,5]],
                 [[0,4], [1,4], [2,4], [3,4], [4,4], [5,4]],
                 [[0,3], [1,3], [2,3], [3,3], [4,3], [5,3]],
                 [[0,2], [1,2], [2,2], [3,2], [4,2], [5,2]],
                 [[0,1], [1,1], [2,1], [3,1], [4,1], [5,1]],
                 [[0,0], [1,0], [2,0], [3,0], [4,0], [5,0]]]

grid_acomodo = []

grid_acomodo = lectura_csv.lectura_csv()  # se rellena la grid con la obtenida del csv

# Recorre la grid una por una para obtener los datos y entonces hacer el 
# recorrido según cordenadas estraidas de vectores
for columna in range(len(grid_acomodo[0])):
    for fila in range(len(grid_acomodo)):
        posicion = grid_espacial[fila][columna]
        # se almacena vector de cada espacio en matriz
        print(posicion)
        # motor.mover(grid_espacial[posicion[0]][posicion[1]]) # se recorre toda
    
        # time.sleep(3)

        # El motor avanza al 5,5
        # motor.mover(grid_espacial[5][5])

