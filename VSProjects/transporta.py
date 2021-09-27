original = [[0,0,0],
            [0,0,0]]

transposta = [[0,0],
              [0,0],
              [0,0]]
              
for i in range (0,2):
    for j in range (0,3):
        original[i] [j] = float(input("Digite um número:"))

for i in range (0,2):
    for j in range (0,3):
        transposta[j] [i] = original[i] [j]


print(original)
print(transposta)
