idade = int(input())
tempo_anual = int(idade/365)
saldo = idade - tempo_anual * 365

meses = int(saldo/30)
dias = saldo - meses * 30

print("{} ano(s)" .format(tempo_anual))
print("{} mes(es)" .format(meses))
print("{} dia(s)" .format(dias))