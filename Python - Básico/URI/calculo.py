entrada1 = input().split(' ')
entrada2 = input().split(' ')

cod, numero, valor = entrada1
cod2, numero2, valor2 = entrada2

total = int(numero)*float(valor)+int(numero2)*float(valor2)
print("VALOR A PAGAR: R$ {:.2F}".format(total))

