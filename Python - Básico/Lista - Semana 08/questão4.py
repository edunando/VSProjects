num = input("Digite um número:")
for n in num:
    if (num.isdigit()) == True:
        break
    else:
        num = input("Digite um número:")
print(num)

