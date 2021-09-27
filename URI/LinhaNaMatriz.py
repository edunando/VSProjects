linha = int(input())
operacao= input()
matriz=[]
for i in range(3):
    matriz.append([])
for i in range(3):
    for j in range(3):
        valor = float(input())
        matriz[i].append(valor)
if operacao == 'S':
    soma = 0
    for k in matriz[linha]:
        soma = soma + k
    print(soma)
if operacao == 'M':
    media = 0
    soma = 0
    for k in matriz[linha]:
        soma = soma + k
    media= soma/12
    print(media)