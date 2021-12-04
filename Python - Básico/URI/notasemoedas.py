valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for cedula in notas:
    quant_cedulas = int(valor/cedula)
    print("{} nota(s) de R$ {:.2f}".format(quant_cedulas, cedula))
    valor -= quant_cedulas*cedula


print("MOEDAS:")
for cedula_1 in moedas:
    quant_moedas = int(round(valor,2)/cedula_1)
    print("{} moeda(s) de R$ {:.2f}".format(quant_moedas, cedula_1))
    valor -= quant_moedas*cedula_1