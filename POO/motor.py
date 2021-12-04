class Motor:
    def __init__(self, motorizacao, combustivel = 'flex'):
        self._motorizacao = motorizacao
        self._combustivel = combustivel

        @property #Método Get, para poder retornar um valor
        def motorizacao(self):
            return self._motorizacao


        @motorizacao.setter #método que vai receber um valor
        def motorizacao(self, nova_motorizacao):
            self._motorizacao = nova_motorizacao


             

if __name__ == '__main__':
    motor = Motor(2.0)

    print(motor)