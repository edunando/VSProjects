numeros = list(range(6))
soma = 0
for i in range(6):
    numeros[i] = int(input("insira seus números aqui:"))
    soma += numeros[i]
media = soma/6
print('Sua média é de: {:.2F}' .format(media))
for i in range(6):
    if media < numeros[i]:
        print("Os números acima da média são:",numeros[i])
