class Guitarra():
    def __init__(self, marca, preço, modelo): #  
        self.marca = marca
        self.preço = preço
        self.modelo = modelo
    
    def __str__(self):
        return f'{self.__class__.__name__} marca {self.marca} modelo: {self.modelo}: R$ {self.preço}'

    def tocar(self):
        return 'ueunnnn uen eunnnnnnnnnnn'

if __name__ == '__main__':
    guitarra = Guitarra('Ibanez', 6900.00, 'RG 350 DXZ')
    print(guitarra)