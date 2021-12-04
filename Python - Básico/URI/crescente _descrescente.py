entrada = input().split()
x = int(entrada[0])
y = int(entrada[1])
while x != y:
           
    if x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')
        
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])