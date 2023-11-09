def qsort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[len(lista)//2]
        menores = [int(i) for i in lista if i < pivo]
        maiores = [int(i) for i in lista if i > pivo]
    return qsort(menores) + [pivo] + qsort(maiores)
lista1 = [int(i) for i in input().split()]
lista2 = [int(i) for i in input().split()]
soma_listas = lista1+lista2
print(qsort(soma_listas))