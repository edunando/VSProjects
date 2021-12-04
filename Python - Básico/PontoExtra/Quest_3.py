numeros = list(range(10))
for i in range(10):
    numeros[i] = int(input("insira seus números aqui:"))
for j in range (0,9):
    if numeros[j] > numeros[i]:
        print('Valores maior do que o último número lido:',numeros[j])
