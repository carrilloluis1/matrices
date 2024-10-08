#1.

def agegar_columna(matriz: list, columna_nueva: list)-> list:
    
    '''En esta funcion agrega una columna nueva a una matriz ya existente
        Recibe como parametro:
        - La matriz
        - Columna que desea ser agregada
        Devuelve una nueva matriz '''
        
    if type(matriz) != list:
        print("La matriz no es una lista")
        return None
    
    if type(columna_nueva) != list:
        print("La columna que quieres agregar no es una lista")
        return None
    
    if len(matriz) != len(columna_nueva):
        print("La cantidad de filas son distintas")
        return None
    
    
    matriz_nueva = []
    
    for i in range(len(matriz)):
        nueva_fila = matriz[i] + [columna_nueva[i]]
        matriz_nueva += [nueva_fila ]

    return matriz_nueva
