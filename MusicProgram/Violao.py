from instrumentos import *


class Violao(Instrumento):
    def __init__(self, fabricante, tipo, cor, numCordas): # Um violão pode ser de 6 cordas, 7 cordas e até 12 cordas, e você pode tocá-lo com palheta ou no dedilhado.
        super().__init__(fabricante,tipo,cor)
        self.numCordas = numCordas

    def __str__(self):
        return f'{super().__str__} Cordas: {self.numCordas}'
    def afinar(self):
        print('afinando o violão...\ndedilhando...\nfa-la-do-sol-si\ndedilhando\ndo-fa-si-re-mi\n dedilhando\nlá-lá-ré-ré-si\ndedilhando\ndó-ré-mi-fá-sol')

    def tocar(self):
        print('Tocando o violão.... DO-RE-MI-FA-SOL...')

    def trocarCorda(numCordas):
        print('Trocando para a próxima Corda...')


class cavaquinho(Violao):
    def __init__(self, fabricante, tipo, cor, numCordas):
        super().__init__(fabricante, tipo, cor, numCordas)
    GRAVE = 1
    MEDIA = 2
    AGUDA = 3

    def tipoAfinacao(self):
        return 'Grave' if self.tipoAfinacao == cavaquinho.GRAVE else ('Media' if self.tipoAfinacao == cavaquinho.MEDIA else 'Aguda')

    def afinar(self): #O tipo da afinação do cavaquinho pode ser ré-lá-si-mi, ré-si-sol-sol, mi-dó#-lá-lá, mi-ré-si-sol.
        print('afinando o cavaquinho... \n  dedilhando... \n fa-la-do-sol-si \ndedilhando \ndo-fa-si-re-mi \n dedilhando \n lá-lá-ré-ré-si \n dedilhando \ndó-ré-mi-fá-sol')

    def tocar(self):
       print('tocando cavaquinho... do-re-mi-fa-sol')
    
    def __str__(self):
        return f'{super().__str__} Cordas: {self.numCordas}'


