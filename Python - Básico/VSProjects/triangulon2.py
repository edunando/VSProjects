def verificatriangulo (valor1, valor2, valor3):
    if (valor1+valor2) >= valor3 and (valor2+valor3) >= valor1 and (valor1+valor3) >= valor2:
       return 1
    return 0    

if verificatriangulo (1,1,1) == 1:
    print("é um triângulo")
else:
    print("não é um triângulo")

def definetipotrangulo (valor1, valor2, valor3):
    if verificatriangulo (valor1, valor2, valor3) == 1:
        print("triângulo equilatero")
    else:
        if valor1 != valor2 and valor2 != valor3 and valor3 != valor1:
            print("triângulo escaleno")
        else:
            print("triângulo isoceles")
    

lado1 = 3
lado2 = 3
lado3 = 3

definetipotrangulo(lado1,lado2,lado3)