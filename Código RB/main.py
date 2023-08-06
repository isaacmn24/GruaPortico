#import time
# Motor.py
import lectura_csv

#motor = Motor()

# Esta matriz contiene las coordenads del espacio físico
# Ahora es un espacio gigante, pero la idea es hacerlo tan preciso como queramos
# Se aceptan otras ideas más eficientes
grid_espacial = []

grid_espacial = lectura_csv.lectura_csv()  # se rellena la grid con la obtenida del csv

# Recorre la grid una por una para obtener los datos y entonces hacer el 
# recorrido según cordenadas estraidas de vectores
for columna in range(len(grid_espacial[0])):
    for fila in range(len(grid_espacial)):
        posicion = grid_espacial[fila][columna]
        # se almacena vector de cada espacio en matriz
        print(posicion)
        #motor.mover(grid_espacial[posicion[0]][posicion[1]]) # se recorre toda
        

#time.sleep(3)

# El motor avanza al 5,5
#motor.mover(grid_espacial[5][5])

