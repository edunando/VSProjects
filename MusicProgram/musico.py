from abc import *
from instrumentos import *
from Saxofone import *
from Violao import *
from Acordeon import *
from time import sleep

class Musico(ABC):
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def addInstrumento(self):
        print('Adicione um Instrumento')
        return 

    def iniciarDesmonstração(self):
        print('Show Iniciado')
        return

    def exibirInstrumentos(self):
        print('Instrumentos Disponiveis:\nSaxofone\nAcordeon\nViolao\nCavaquinho')
        return

