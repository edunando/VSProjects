from FormaGeometrica import *

class Losango(FormaGeometrica):
    def __init__(self, nome, D, d):
        super().__init__(nome)
        self.diagonalMaior = D
        self.diagonalMenor = d


    def calculaArea(self):
        return (self.diagonalMaior * self.diagonalMenor) /2

    # sem polimorfismo
    def areaLosango(self):
        return (self.diagonalMaior * self.diagonalMenor) /2
        
        


