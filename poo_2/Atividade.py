from abc import ABC, abstractmethod

class Academia_de_Batalha(ABC): #Aventureiros da Guilda

    def __init__(self,nome,tipo="espadachim"):
        self.nome = nome
        self.tipo = tipo

    @abstractmethod
    def atacar(self):
        pass

    def __str__(self):
        return f'Olá! Sou eu sou um {self.__class__.__name__}, um espadachim do tipo {self.tipo}'

class Espadachim_de_gelo(Academia_de_Batalha):

    def __init__(self, nome, tipo="espadachim"):
        super().__init__(nome,tipo)

    def atacar(self):
        print('Encare a fúria dos ventos gelados do Lich Rei!')

class Espadachim_de_fogo(Academia_de_Batalha):

    def __init__(self, nome, tipo="espadachim"):
        super().__init__(nome, tipo=tipo)

    def atacar(self):
        print('Sinta a chama da ira de Malfurion Tempesfúria!')

class Espadachim_de_agua(Academia_de_Batalha):
    def __init__(self, nome, tipo="espadachim"):
        super().__init__(nome, tipo=tipo)

    def atacar(self):
        print('Sinta o verdadeiro poder dos mares!')


Espadachim1 = Espadachim_de_gelo('Raveus', 'Espadachim de gelo')
Espadachim2 = Espadachim_de_fogo('Xinglang','Espadachim do Fogo do norte')
Espadachim3 = Espadachim_de_agua('Yumeko','Espadachim aprendiz de Poseidon')
##print('Espadachim de Gelo Vs Espadachim da Agua! Lutem!')
##Espadachim1.atacar()
##Espadachim3.atacar()

for obj in [Espadachim1,Espadachim2,Espadachim3]:
    print(obj)
    obj.atacar()