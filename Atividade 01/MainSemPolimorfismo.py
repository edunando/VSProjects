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


# FormaGeometrica, Triangulo, Trapezio, Losango e Circulo sao colocados */
for obj in poligono:
    if (isinstance(obj,Triangulo)):
        areaTotal += obj.areaTriangulo()
        print(obj.__class__.__name__ + ':' + str(obj.areaTriangulo()))
        
    elif (isinstance(obj,Trapezio)):
        areaTotal += obj.areaTrapezio()
        print(obj.__class__.__name__ + ':' + str(obj.areaTrapezio()))
        
    elif (isinstance(obj,Circulo)):
        areaTotal += obj.areaCirculo()
        print(obj.__class__.__name__ + ':' + str(obj.areaCirculo()))
        
    elif (isinstance(obj,Losango)):
        areaTotal += obj.areaLosango()
        print(obj.__class__.__name__ + ':' + str(obj.areaLosango()))

    elif( isinstance(obj,FormaGeometrica) ): 
        areaTotal += obj.areaFormaGeometrica()
        print(obj.__class__.__name__ + ':' + str(obj.areaFormaGeometrica()))
        

    
print(f'Area Total: {areaTotal:.2f}')
