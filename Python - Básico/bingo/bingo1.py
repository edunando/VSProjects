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

def verificar(l1,l2):
    listaNumerosContidos = []
    quantidadeNumerosContidos = 0
    for i in l1:
        if(i in l2) and (i not in listaNumerosContidos):
            quantidadeNumerosContidos += 1
            listaNumerosContidos.append(i)
    return quantidadeNumerosContidos
    
def contido (n,lista):
    Contido = False
    if n in lista:
        Contido = True
    return Contido

def inserir(n,lista):
    if contido(n, lista) == False:
        lista.append(n)
        return True
    else:
        return False


def limpar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
