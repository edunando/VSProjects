def menor(lista):
    valores = []
    menor = valores[0]
    for menorvalor in lista:
        if menorvalor > menor:
            menorvalor = menor
    return valores

numeros = []
for i in range(0, 10):
    num = int(input())
    numeros.append(num)

print(menor(numeros))
