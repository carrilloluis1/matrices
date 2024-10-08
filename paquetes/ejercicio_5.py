#5.

def calcualr_media(lista: list) -> int:
    
    '''Función que calcula la media de cualquier lista:
    Recibe como parámetro una lista'''
    
    suma_edades = 0 
    contador = 0
    
    if type(lista) != list:
        print('El parámetro no es una lista')
        return None

    for i in range(len(lista)):
        if type(lista[i]) != int and type(lista[i]) != bool:
            print(' los datos de la lista no son números')
            return None


    for i in range(len(lista)):
        suma_edades += lista[i]
        contador += 1
    
    if contador > 0:
        media_etaria = suma_edades / contador
    else:
        media_etaria = 0
    
    return media_etaria

