from typing import Counter, List
def novo(n1, n2):   
    from random import randint
    randomlist = list()
    cont = 0
    while True:
        num = randint(n1,n2)
        if num not in randomlist:
            randomlist.append(num)
            cont +=1
        if cont >= 6:
            break
    return randomlist
def contido (n,lista):
    if n in lista:
        print("Está contido")
    else:
        print("Não está contido")
def verificar(l1,l2):
    cont = 0
    for i in range (len(l1)):
        for j in range (len(l2)):
            if l1[i] == l2[j]:
                cont += 1
                break
    print(f'Na lista 2, há {cont} valores da lista 1')
    return cont
def inserir(n,lista):
    if n not in lista:
        lista.append(n)
        print(f'o número {n} foi inserido com sucesso!')
    else:
        print(f'o número {n} não foi inserido na lista, pois ja está contido nela. Encerrando o Programa.')
    return n

