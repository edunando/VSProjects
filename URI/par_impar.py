valor_x = 2
contador = 0
soma = 0
cont_impar = 0
cont_positivo = 0
cont_negativo = 0

for n in range(5):
    valores = int(input())
    if (valores % valor_x == 0):
        contador += 1
    if (valores % valor_x != 0):
        cont_impar += 1
    if (valores > 0):
        cont_positivo += 1
    if (valores < 0):
        cont_negativo += 1

print("{} valor(es) par(es)" .format(contador))        
print("{} valor(es) impar(es)" .format(cont_impar))
print("{} valor(es) positivo(s)" .format(cont_positivo))
print("{} valor(es) negativo(s)" .format(cont_negativo))
