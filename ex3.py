def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
        else:
            menor = lista[i]
    return f'Maior:{maior} | Menor:{menor}'

maior_menor([1,2,3,4,5])