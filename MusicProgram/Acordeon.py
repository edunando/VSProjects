from instrumentos import *

class Acordeon(Instrumento):

    def __init__(self, fabricante, tipo, cor,numBaixo,numRegistros,): # Existem acordeons de 80 baixos e 120 baixos 
        super().__init__(fabricante, tipo, cor)
        self.numBaixo = numBaixo
        self.numRegistros = numRegistros # Os registros do acordeon são teclas que modificam o som (estilo flauta, clarinete, violino, saxofone, etc.). 
        #Para tocar, é necessário fazer movimentos de abrir e fechar o fole para produzir o som da nota musical.
        #No caso do Acordeon, vamos considerar que só é possível tocar 5 notas musicais em cada abertura ou fechamento do fole.

    def __str__(self):
        return f'{super().__str__} Num de Baixo: {self.numBaixo} Num de Registros: {self.numRegistros}'

    def afinar(self):
        print('Afinando o acordeon \n  dedilhando... \n fa-la-do-sol-si \ndedilhando \ndo-fa-si-re-mi \n dedilhando \n lá-lá-ré-ré-si \n dedilhando \ndó-ré-mi-fá-sol')

    def tocar(musica):
       print('tocando Arcodeon...')

    def puxarFole(self):
        print('Puxando o fole...')





