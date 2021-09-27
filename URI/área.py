import math
entrada = input().split(' ')
A, B, C = entrada
pi = 3.14159


a_triangulo = float(A) *float(C)/2
a_circulo = pi*float(C)**2
a_trapezio = (float(A)+float(B))*float(C)/2
a_quadrado = float(B)**2
a_retangulo = float(A)*float(B)

print("TRIANGULO: {:.3f}".format(a_triangulo)) 
print("CIRCULO: {:.3f}".format(a_circulo)) 
print("TRAPEZIO: {:.3f}".format(a_trapezio))
print("QUADRADO: {:.3f}".format(a_quadrado)) 
print("RETANGULO: {:.3f}".format(a_retangulo))

