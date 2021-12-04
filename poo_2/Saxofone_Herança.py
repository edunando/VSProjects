class Saxofone():
    def __init__(self, marca, preço, tipo): # tipo: soprano, baritono, alto, tenor, 
        self.marca = marca
        self.preço = preço
        self.tipo = tipo
    
    def __str__(self):
        return f'{self.__class__.__name__} marca {self.marca} tipo {self.tipo}: R$ {self.preço}'

    def tocar(self):
        return 'tchu ru ru ruuuuuu'

if __name__ == '__main__':
    sax = Saxofone('Yamaha', 8900.00, 'Alto')
    print(sax)


