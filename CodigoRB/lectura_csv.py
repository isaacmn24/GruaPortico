import csv
import os

# Ruta de la carpeta donde se encuentra el archivo CSV
ruta_carpeta = r'C:\Users\luisc\OneDrive - Estudiantes ITCR\Escritorio\Micros\Proyecto_GP\GruaPortico\Código RB'
# Cambiar el directorio de trabajo actual a la carpeta deseada
os.chdir(ruta_carpeta)

grid_espacial_simpli = [[[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0] ],
                        [[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0] ],
                        [[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0] ],
                        [[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0] ],
                        [[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0] ]]

lista_csv = []

def lectura_csv():
    escritura = 0

    # lectura del archivo csv
    with open('CSV_posiciones.csv', 'r') as archivo:
        
        csvPosiciones = csv.reader(archivo)
        next(csvPosiciones)  # se salta la primera fila
    
        lista_csv.extend(csvPosiciones)  # Se el csv a una lista 
        # (lista de vectores)

        # se recorre la matris grid y se agrega uno por uno los datos de la 
        # lista, se llena por columnas
        for columna in range(len(grid_espacial_simpli[0])):
            for fila in range(len(grid_espacial_simpli)):
                    grid_espacial_simpli[fila][columna] = lista_csv[escritura]
                    escritura = escritura + 1
                    
                    
    return grid_espacial_simpli


        