n_pares = 0
pares = []
while (True):
    if n_pares == 6:
        break
    numeros=int(input('Insira seu número: '))
    if numeros % 2 == 0:
        pares.append(numeros)
    if numeros % 2 == 0:
        n_pares += 1
print('Seus números pares são:', pares)