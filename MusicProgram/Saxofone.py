from instrumentos import *

class Sax(Instrumento):
    def __init__(self, fabricante, tipo, cor, modelo): #Os tipos do Saxofone podem ser (Alto, tenor, barítono e baixo)
      super().__init__(fabricante,tipo,cor)
      self.modelo = modelo

    def __str__(self):
        return f'{super().__str__()} Modelo : {self.modelo} '

    def afinar(self):
        print (f'abre o fole \n lá-si-dó-ré-mi \n puxa o fole\n mi-fá-sol-lá-sol \n abre o fole \n si-si-ré-ré-mi \n fecha o fole \n fá-fá-sol-si-sol')
        return

    def tocar(self):
        print('tocando Sax')
        return

    def limpar(self):
        print('limpando instrumento...')
        return

    def soprar(self):
        print('soprando... shhhh')
        return
