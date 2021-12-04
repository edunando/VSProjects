p = int(input())
t = int(input())
qtde = 0
tabuleiro = []
for i in range(t):
    tabuleiro.append([0] * t)

for i in range(t):
    linha, coluna = input().split()
    linha, coluna = int(linha), int(coluna)

if tabuleiro[linha][coluna] == 0:   
        qtde += 1
        tabuleiro[linha][coluna] = 1

if (qtde == t):
    print('True')
else:
    print('False')
print(qtde)