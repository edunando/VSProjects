numeros = int(input())
tamanho = int(input())
borda = []
lado = 0
jogo = False

for c in range(tamanho):
    borda.append([0] * tamanho)

for d in range(numeros):
    posX, posY = input().split()
    posX = int(posX)
    posY = int(posY)

    if borda[posX][posY] != 0:
        pass
    else:
        borda[posX][posY] = 1
        lado += 1

if lado == numeros:
    jogo = True
    print('{}\n0'.format(jogo))
else:
    print('{}\n{}'.format(jogo, (numeros - lado)))