frase = input()
cont = 0
for i in range(58, 127):
    for j in range(32, 47):
        if chr(i) in frase or chr(j) in frase:
            cont += 1
if cont > 0:
    print('Não')
else:
    print('Sim')
     