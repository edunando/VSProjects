# ler a entrada P
n_pecas = int(input())

# ler a entrada T
_ = int(input())

# ler a entrada das peças
pecas = []
for i in range(n_pecas):
    pecas.append(input().split())  

# usa um dict para fazer o controle das peças já inseridas 
tabuleiro = {}

# quantidade de peças que não pode ser inserida no tabuleiro
pecas_nao_inseridas = 0


while pecas:
  # remove uma peça da lista
  posicao_peca = pecas.pop()

  # cria uma chave -> [1,1] -> "1*1" 
  key = "*".join(posicao_peca)

  # pega o valor armazenado pela chave (key) no dict 
  v = tabuleiro.get(key)

  # se a peca ja foi inserida
  if v: 
    # soma as pecas que nao foram inseridas
    pecas_nao_inseridas+=1
  else:
    # se nao, inseri a peça no tabuleiro
    tabuleiro[key] = 1

# verifica se alguma peça não foi inserida
if pecas_nao_inseridas > 0:
  print(False)
else:
  print(True)

# printa as a quantidade de peças que não foram inseridas
print(pecas_nao_inseridas)