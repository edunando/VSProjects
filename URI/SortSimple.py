numeros_entrada = input().split()

valores=[int(i) for i in numeros_entrada]

valores.sort()

print(*valores, sep='\n')
print()
print(*numeros_entrada, sep='\n')
