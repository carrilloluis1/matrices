#2 Crear una función que imprima por pantalla el tamaño de una matriz

def calcular_tamaño_matriz(matriz: list)-> None:
    
    '''
    Función que muestra el tamaño de la matriz
    recibe por parámetro:
    La matriz
    retorna el tamaño
    
    '''
    
    if type(matriz) != list:
        print("El parametro no es una lista")
        return None
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    print(f'La matriz es de tamaño {filas} x {columnas}.')
