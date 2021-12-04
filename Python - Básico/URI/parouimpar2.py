casos = int(input())
testes = ['']
for i in range(1,(casos+1)):
    testes.append(int(input()))


for i in range(1,(casos+1)):
    if(testes[i] % 2 == 0) and (testes[i] > 0):
        print('EVEN POSITIVE')
    elif(testes[i] % 2 == 0) and (testes[i] < 0):
        print('EVEN NEGATIVE')
    elif(testes[i] % 2 != 0) and (testes[i] > 0):
        print('ODD POSITIVE')
    elif(testes[i] % 2 != 0) and (testes[i] < 0):
        print('ODD NEGATIVE')
    else:
        print('NULL')
