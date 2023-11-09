def soma_lista(lista):
    if lista == []:
        return 0
    return lista[0] + soma_lista(lista[1:])

def media_lista(lista):
    return soma_lista(lista)//len(lista)

media_lista([1,2,3,4,5])