from abc import ABC, abstractmethod

class Instrumento(ABC):

    def __init__(self,fabricante,tipo,cor):
        self.fabricante = fabricante
        self.tipo = tipo
        self.cor = cor

    @abstractmethod
    def afinar(self):
        pass

    def __str__(self):
        return f'> Afinando o {self.__class__.__name__}...'


    def tocar(musica):
        pass


class Sax(Instrumento):
    def __init__(self, fabricante, tipo, cor, modelo):
      self.fabricante = fabricante
      self.tipo = tipo
      self.cor = cor
      self.modelo = modelo

    def __str__(self):
        return f'{self.__class__.__name__} Modelo : {self.modelo} Fabricante: {self.fabricante} tipo: {self.tipo} cor: {self.cor}'

    def afinar(self):
        print(f'abre o fole \n lá-si-dó-ré-mi \n puxa o fole\n mi-fá-sol-lá-sol \n abre o fole \n si-si-ré-ré-mi \n fecha o fole \n fá-fá-sol-si-sol')

    def tocar(musica):
        print('{__clas__.__name__} tocando Sax')

    def limpar(self):
        print('limpando instrumento...')

    def soprar(self):
        print('soprando... shhhh')

class Violao(Instrumento):
    def __init__(self, fabricante, tipo, cor, numCordas):
      self.fabricante = fabricante
      self.tipo = tipo
      self.cor = cor
      self.numCordas = numCordas

    def __str__(self):
        return f'{self.__class__.__name__} fabricante: {self.fabricante} tipo: {self.tipo} cor: {self.cor} Cordas: {self.numCordas}'
    def afinar(self):
        print(f'afinando o violão... \n  dedilhando... \n fa-la-do-sol-si \ndedilhando \ndo-fa-si-re-mi \n dedilhando \n lá-lá-ré-ré-si \n dedilhando \ndó-ré-mi-fá-sol')

    def tocar(musica):
        print('{__class__.__name__} tocando violão')

    def trocarCorda(numCordas):
        print(f'O número de cordas são {numCordas}.... Trocando para a próxima...')

class cavaquinho(Violao):
    def tipoAfinacao(self):
        pass

    def afinar(self):
        pass

    def tocar(musica):
        print('{__class__.__name__} tocando cavaquinho')

class Acordeon(Instrumento):

    def __init__(self, fabricante, tipo, cor,numBaixo,numRegistros,):
     self.fabricante = fabricante
     self.tipo = tipo
     self.cor = cor
     self.numBaixo = numBaixo
     self.numRegistros = numRegistros

    def __str__(self):
        return f'{self.__class__.__name__} fabricante: {self.fabricante} tipo: {self.tipo} cor: {self.cor} Num de Baixo: {self.numBaixo} Num de Registros: {self.numRegistros}'

    def afinar(self):
        print(f'Afinando o acordeon \n  dedilhando... \n fa-la-do-sol-si \ndedilhando \ndo-fa-si-re-mi \n dedilhando \n lá-lá-ré-ré-si \n dedilhando \ndó-ré-mi-fá-sol')

    def tocar(musica):
        print('{__class__.__name__} tocando Arcodeon.')

    def puxarFole(self):
        pass


class Musico(ABC):
    Instrumentos = [Violao,cavaquinho,Acordeon,Sax]
    def __init__(self, nome, nacionalidade,instrumentosUtilizados):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self._instrumentosUtilizados = []

    def addInstrumento(self, Instrumento):
        self._instrumentosUtilizados.append (Instrumento)

    def exibirInstrumentos (self):
        print(self._instrumentosUtilizados)
