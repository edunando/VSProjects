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

#sorteio
v1 = int(input('Valor mínimo a ser gerado: '))
v2 = int(input('Valor máximo a ser gerado: '))
print()
print(f'Os números gerados entre {v1} e {v2} foram:',novo(v1,v2))
print()
#contido
list_ = list(range(0,50 +1))
numeral = int(input('Qual número você quer checar se está na lista?: '))
print()
contido(numeral,list_)
print()
#verificar
lista2 = list(range(32,91))
print('Checando valores das duas listas...')
print()
verificar(list_,lista2)
#inserir
print()
inserir_num = int(input('Insina o número:'))
inserir(inserir_num,list_)    