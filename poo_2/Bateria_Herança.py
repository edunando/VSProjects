class Bateria():
    GRAVE = 1
    MEDIA = 2
    AGUDA = 3
    def __init__(self, marca, preço, afinação): # afinação: grave, media, aguda
        self.marca = marca
        self.preço = preço
        self.afinação = afinação
        

    def getAfinação(self):
        return 'Grave' if self.afinação == Bateria.GRAVE else ('Media' if self.afinação == Bateria.MEDIA else 'Aguda')
    
    def __str__(self):
        return f'{self.__class__.__name__} marca {self.marca} afinação {self.getAfinação()}: R$ {self.preço} '

    def tocar(self):
        return 'Tum tum pa, tum tum pa'

if __name__ == '__main__':
    bateria = Bateria('RMV', 2900.00, Bateria.MEDIA)
    print(bateria)
