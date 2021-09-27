entrada= input().split(" ")

codigo = int(entrada[0])
quantidade = int(entrada[1])
preço = 0.0

if codigo ==1:
    preço = 4.0 * quantidade
elif codigo == 2:
    preço = 4.5 * quantidade
elif codigo == 3:
    preço = 5.0 * quantidade
elif codigo == 4:
    preço = 2.0 * quantidade 
elif codigo == 5:
    preço = 1.5 * quantidade

print("Total: R$ %0.2f" %preço)