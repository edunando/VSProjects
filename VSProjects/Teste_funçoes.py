# LOCAL DAS FUNÇÕES
def divisores(n):
    resultado = [i for i in range(1, n + 1) if n % i == 0]
    return resultado
def primo(n):
    resultado = [i for i in range(1, n + 1) if n % i == 0]
    return resultado
def menor(lista):
    menor_lista = lista[0]
    for i in range(1,len(lista)):
        if lista[i] < menor_lista:
            menor_lista = lista[i]
    return menor_lista
def especial(st):
    ascii_list = [chr(i) for i in range(32,48)]
    chr_e = 0
    for i in range (len(st)):
        if st[i] in ascii_list:
            chr_e += 1
    return chr_e
def distintos(lista):
    ds = True
    for i in range(0, len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                ds = False
        if ds == False:
            break
    return ds
##########################################################
#Divisores e primos#
num = int(input('Digite aqui seu número: '))
divisores(num)
print(primo(num))
#Menor e Distintos#
lista = []
Lista_Qtde = int(input(' Digite aqui a quantidade de caracteres da sua lista: '))
for i in range(0, Lista_Qtde):
    numeros = int(input('Digite aqui seu número:'))
    lista.append(numeros)
print(menor(lista))
print(distintos(lista))
#Caracteres Especiais#
w = input('Digite aqui sua frase: ')
print(especial(w))