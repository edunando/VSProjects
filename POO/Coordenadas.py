class Ponto:
    def __init__ (self, x, y):
        self.x=x
        self.y=y

    def quadrante(self):
        if(self.x > 0 and self.y > 0):
            return '1º quadrante'
        elif (self.x < 0 and self.y > 0):
            return '2º quadrante'
        elif (self.x < 0 and self.y < 0):
            return '3º quadrante'
        elif (self.x > 0 and self.y < 0):
            return '4º quadrante'

        else:
            return 'Nenhum dos quadrantes'
ponto1 = Ponto(1,2)
print('Coordenadas do ponto 1: (%d,%d)'%(ponto1.x,ponto1.y))
print(f'Ponto 1 pertence ao {ponto1.quadrante()}')
