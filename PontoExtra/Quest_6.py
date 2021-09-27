numeros =list()   
distintos = 0
while True:
    entrada = int(input('Insira aqui os Valores:'))
    if entrada not in numeros:
        numeros.append(entrada)
        distintos += 1
        if distintos >= 6:
            break
print(numeros)