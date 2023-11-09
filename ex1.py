def conta_valor(lista, valor):
    cont = 0
    for i in range(len(lista)):
        if lista[i] == valor:
            cont += 1
    return cont
conta_valor([1,2,3,4,2], 0)