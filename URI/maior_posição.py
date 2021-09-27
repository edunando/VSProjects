maior = 0
posicao = 0
lista = {}

for posicao in range(1,10):
  valor = int(input())
  if (valor > maior):
      maior = valor
      lista[valor] = posicao
  posicao += 1

print(maior)
print(lista[maior])
