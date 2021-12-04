from FormaGeometrica import *
from Trapezio import *
from Triangulo import *
from Circulo import *
from Losango import *

areaTotal = 0

poligono = [Trapezio("Trapezio", 4, 3,2), Triangulo("Triangulo",4,2)]
poligono.append(Circulo("Circulo",3))
poligono.append(Losango("Losango",5,3))
poligono.append(FormaGeometrica("FormaGeometrica (Superclasse)"))

# Poligono, Triangulo, Trapezio, Losango e Circulo sao colocados */
for obj in poligono:
    areaTotal += obj.calculaArea()
    print(obj.__class__.__name__ + ':' + str(obj.calculaArea()))
            
print(f'Area Total: {areaTotal:.2f}')


a = Trapezio("Trapezio", 4, 3,2)
b = Triangulo("Triangulo",4,2)
print(a.calculaArea())
a = b
print(a.calculaArea())
