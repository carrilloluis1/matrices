# 4
def calcular_media_etaria(lista_edades: list, lista_generos: list, lista_nombres: list)-> list:
    
    suma_hombres = 0
    contador_hombres = 0
    suma_mujeres = 0
    contador_mujeres = 0

    for i in range(len(lista_generos)):
        
        if lista_generos[i] == "Hombre":
            
            suma_hombres += lista_edades[i]
            contador_hombres += 1
            
        elif lista_generos[i] == "Mujer":
            
            suma_mujeres += lista_edades[i]
            contador_mujeres += 1

    if contador_hombres > 0:
        media_etaria_hombre = suma_hombres / contador_hombres
    else:
        media_etaria_hombre = 0

    if contador_mujeres > 0:
        media_etaria_mujer = suma_mujeres / contador_mujeres
    else:
        media_etaria_mujer = 0
    
    resultado = [media_etaria_hombre , media_etaria_mujer]
    
    return resultado
