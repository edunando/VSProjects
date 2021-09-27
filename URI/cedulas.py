valor = int(input())
print(valor)
notas = [100, 50, 20, 10, 5, 2, 1]

for cedula in notas:
    quant_cedulas = int(valor/cedula)
    print("{} nota(s) de R$ {},00".format(quant_cedulas, cedula))
    valor -= quant_cedulas*cedula
