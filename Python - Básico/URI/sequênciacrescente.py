entrada=1
while True:
    X = int(input())
    if X == 0:
        break
    entrada = 1
    while entrada <= X:
        if entrada==X:
            print('%d'%(entrada),end="\n")
        else:
            print('%d'%(entrada),end=" ")
        entrada+=1