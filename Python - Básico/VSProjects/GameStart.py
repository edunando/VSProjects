p = int(input())
t = int(input())
qtde = 0
m = list()

for i in range(t):
        m.append([])
        for j in range(t):
            m[i].append(0)
for i in range(t):
    linha, coluna = input().split()
    linha, coluna = int(linha), int(coluna)
    if m[coluna] in range(t) :
        qtde += 1
    else:
       m.insert(linha,coluna)
if (qtde > 0):
    print('False')
else:
    print('True')
print(qtde)
print(m)