p = input("Insira uma frase: ")
cont = 0
for e in p:
    if (e.isalnum()) == False:
        cont += 1
print(f" {cont} caracteres especiais.")