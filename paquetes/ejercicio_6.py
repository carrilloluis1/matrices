lista = [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]

def encontrar_menor(lista: list) -> list:
    
    cantidad_menores = (len(lista) * 20) // 100

    lista_menores = [0] * cantidad_menores
    
    for i in range(len(lista)):
        for j in range(len(lista)):
            
            if lista[i] == lista[j]:
                break
            
            elif lista[i]< lista[j]:
                lista_menores += [lista[i]]
                break

    return lista_menores

print(encontrar_menor(lista))

