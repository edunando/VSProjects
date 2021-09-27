alcool = 0
gasolina = 0
diesel = 0
print("1 - Álcool")
print("2 - Gasolina")
print("3 - Diesel")
print("4 - Fim")
codigo = 0
while (codigo != 4):
    codigo = int(input("Insira o tipo de Combustivel: "))
    if (codigo == 1):
        alcool += 1
    if (codigo == 2):
        gasolina += 1   
    if (codigo == 3):
        diesel += 1
print("MUITO OBRIGADO")
print("Alcool: {}" .format(alcool))
print("Gasolina: {}" .format(gasolina))
print("Diesel: {}".format(diesel))
#codigo = input("Insira o tipo de Combustivel: ")