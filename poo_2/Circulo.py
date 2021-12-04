from FormaGeometrica import *
import math

class Circulo(FormaGeometrica):
    def __init__(self, nome, raio):
        super().__init__(nome)
        self.raio = raio

    def calculaArea(self):
        return math.pi * self.raio ** 2


    # sem polimorfismo
    def areaCirculo(self):
        return math.pi * self.raio ** 2
