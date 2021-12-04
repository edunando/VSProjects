n_pecas = int(input())
_ = int(input())
pecas = []
for i in range(n_pecas):
    pecas.append(input().split())  
tabuleiro = {}
pecas_nao_inseridas = 0
while pecas:
  posicao_peca = pecas.pop()
  key = "*".join(posicao_peca)
  v = tabuleiro.get(key)
  if v: 
    pecas_nao_inseridas+=1
  else:
    tabuleiro[key] = 1
if pecas_nao_inseridas > 0:
  print(False)
else:
  print(True)
print(pecas_nao_inseridas)