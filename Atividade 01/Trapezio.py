from FormaGeometrica import *

class Trapezio(FormaGeometrica):
    def __init__(self, nome, B, b, h):
        super().__init__(nome)
        self.baseMaior = B
        self.baseMenor = b
        self.altura = h

    def calculaArea(self):
        return ((self.baseMaior + self.baseMenor) * self.altura)/2

    # sem polimorfismo
    def areaTrapezio(self):
        return ((self.baseMaior + self.baseMenor) * self.altura)/2
