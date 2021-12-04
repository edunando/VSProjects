b = float(input())

if  0 <= b <=25:
    print("Intervalo [0,25]")
else:
    if 25 <= b <=50:
        print("Intervalo [25,50]")
    else:
        if 50<= b <= 75:
            print("Intervalo [50,75]")
        else:
            if  75 <= b <= 100:
                print("Intervalo (75,100]")
            else:
                if 0 > b > 100:
                    print("Fora de Intervalo")
################################################################################################
y = float(input())
if 0<= y <= 25:
    print('Intervalo [0,25]')
if 25< y <= 50:
    print('Intervalo (25,50]')
if 50< y <= 75:
    print('Intervalo (50,75]')
if 75< y <= 100:
    print('Intervalo (75,100]')
if y >100 or y <0:
    print('Fora de intervalo')