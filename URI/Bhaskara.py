import math

entrada = input().split(" ")

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

delta = B*B - 4 * A * C

if delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    R1 = (-B + math.sqrt(delta))/(2*A)
    R2 = (-B - math.sqrt(delta))/(2*A)
    print("R1 = %0.5F" %R1)
    print("R2 = %0.5F" %R2)

  