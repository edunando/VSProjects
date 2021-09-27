notas = 0
x=0
media=0
while notas!=2:
    x = float(input())
    if x>=0 and x<=10:
        media+=x/2
        notas+=1
    else:
        print('nota invalida')


print('media = {:.2F}'.format(media))