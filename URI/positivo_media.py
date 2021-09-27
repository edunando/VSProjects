contador = 0
soma = 0


for num in range(6):
    numero = float(input())
    if (numero > 0.0):
        contador += 1
        soma += numero
print(contador, "valores positivos")
print("{:.1f}" .format(soma/contador))
