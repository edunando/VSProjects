nome = input()
salario = float(input())
vendas = float(input())

bonus = vendas * 0.15

salario += bonus

print("TOTAL = R$ %0.2F "%salario)