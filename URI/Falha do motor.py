n_medidas = int(input())
rotacoes = []
rotacoes = input().split()
falhas = 0
for i in range (1, n_medidas):
    if (int(rotacoes[i-1]) > int(rotacoes[i])):
        falhas = i + 1
        break
print(falhas)
