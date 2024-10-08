# 3.Inicializar una matriz de 4 columnas y 4 filas. Cargar en cada cruce de fila y columna el
# valor correspondiente a la multiplicación del índice de fila y columna.

def inicializar_matriz(filas: int = 4, columnas: int = 4, valor_inicial: any = 0) -> list:
    
    matriz = []
    
    for _ in range(filas):
        
        filas_matriz = [valor_inicial] * columnas
        
        matriz += [filas_matriz]
        
    return matriz


matriz = inicializar_matriz()

def cargar_matriz(matriz: list) -> list:
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = i*j
    
    return matriz
