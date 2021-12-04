def novo(n1, n2):
    import random
    if n2 < n1:
        print('Parâmetros não adequados')
    else:
        lista = []
        contador = 0
        while contador < 6:
            numero = random.randint(n1, n2)
            if numero not in lista:
                lista.append(numero)
                contador +=1
        return lista
        #print(lista)
    
def contido(n, lista):
    estaContido = False
    if n in lista:
        estaContido = True
    return estaContido

def verificar(l1, l2):
    listaNumerosContidos = []
    quantidadeNumerosContidos = 0
    for i in l1:
        if(i in l2) and (i not in listaNumerosContidos):
            quantidadeNumerosContidos += 1
            listaNumerosContidos.append(i)
    return quantidadeNumerosContidos

def inserir(n, lista):
    if contido(n, lista) == False:
        lista.append(n)
        return True
    else:
        return False

