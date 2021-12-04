from motor import Motor

class Carro:
    def __init__(self,cor,placa,motor):
        self._cor = cor
        self._placa = placa
        self._motor = motor

    @property
    def cor(self):
        return self._cor
    @cor.setter
    def cor (self,nova_cor):
        self.cor = nova_cor

    def __str__(self):
        return 'Cor: {}, Placa: {}, Motor: {} '.format(self._cor,self._placa,self._motor)

if __name__ == '__main__':
    motor = Motor(1.8,'Gasolina')
    carro = Carro('Preto','VSF-666',2.0)

print(carro)
