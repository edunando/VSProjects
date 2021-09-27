temperatura = 0
quantidade = 0
somatorio = 0

while temperatura != 999:
    temperatura = float(input("Digite 999 para sair ou digite uma temperatura:"))

    if temperatura != 999:
        somatorio += temperatura
        quantidade += 1

media = somatorio / quantidade

print("Sua média é de:",media,)