from funciones import *

def multiplicar_matrices(matriz_uno: list, matriz_dos: list) -> list:
    
    if type(matriz_uno) != list:
        print('La matriz uno no es una lista')
        return None
    
    if type(matriz_dos) != list:
        print('La segunda matriz no es una lista')
        return None
    
    filas_uno = len(matriz_uno)
    columnas_uno = len(matriz_uno[0])
    filas_dos = len(matriz_dos)
    columnas_dos = len(matriz_dos[0])
    
    if columnas_uno != filas_dos:
        print("No se puede realizar la operación")
        return None
    
    matriz_resultado = inicializar_matriz(filas_uno, columnas_dos)

    for i in range(filas_uno):
        for j in range(columnas_dos):
            for k in range(columnas_uno): 
                matriz_resultado[i][j] += matriz_uno[i][k] * matriz_dos[k][j]

    return matriz_resultado

