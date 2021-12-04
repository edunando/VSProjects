from abc import ABC, abstractmethod

class Instrumento(ABC):
    def __init__(self,fabricante,tipo,cor):
        self.fabricante = fabricante
        self.tipo = tipo
        self.cor = cor

    
    def afinar(self):
        print ('fiiiiinnn')
        return

    def __str__(self):
        return f'>{self.__class__.__name__} fabricante: {self.fabricante} tipo: {self.tipo} cor:{self.cor}'


    def tocar(self):
        print('FUEEEUN FUEEUNNN FUEUUUN')
        return




