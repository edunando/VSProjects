C = int(input())
operacao= input()
matriz=[]
for i in range(12):
    matriz.append([])
for i in range(12):
    for j in range(12):
        valor = float(input())
        matriz[i].append(valor)
if operacao == 'S':
    soma = 0
    for k in range(12):
        soma = soma + matriz[k][C]
    print(soma)
if operacao == 'M':
    media = 0
    soma = 0
    for k in range(12):
        soma = soma + matriz[k][C]
    media= soma/12
    print('{:.1f}'.format(media))