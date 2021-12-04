from abc import ABC, abstractmethod

class Instrumento(ABC):
    def __init__(self,fabricante,tipo,cor):
        self.fabricante = fabricante
        self.tipo = tipo
        self.cor = cor


    def afinar(self):
        print('Fiun fiun fiun afinando')
        return

    def tocar(self):
        print('Tocando musiquinha')
        return
    
    def __str__(self):
        return f'O Instrumento ele é feito pelo fabricante {self.fabricante}, ele tem a cor {self.cor} do tipo {self.tipo}.'


class Violao(Instrumento):
    def __init__(self, fabricante, tipo, cor,numCordas):
        super().__init__(fabricante, tipo, cor)
        self.numCordas = numCordas


