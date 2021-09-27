novo = 1
inter_gols = 0
gremio_gols = 0
empate = 0
grenais = 0

while novo == 1:
  gols = input().split(" ")
  inter = int(gols[0])
  gremio = int(gols[1])
  if inter > gremio:
    inter_gols+= 1
  elif gremio > inter:
    gremio_gols+= 1
  elif inter == gremio:
    empate+= 1
  grenais+= 1
  print("Novo grenal (1-sim 2-nao)")
  novo = int(input())

print("%d grenais" %grenais)
print("Inter:%d" %inter_gols)
print("Gremio:%d" %gremio_gols)
print("Empates:%d" %empate)
if inter_gols > gremio_gols:
  print("Inter venceu mais")
elif gremio_gols > inter_gols:
  print("Gremio venceu mais")
else:
  print("Nao houve vencedor")