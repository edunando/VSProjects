class Player():
    def __init__(self,nickname,elementos_magia):
        self._nickName = nickname
        self._magia = elementos_magia

    def get_nickName (self):
        return self._nickName

    def set_nickname (self,Novonickname):
        self._nickName = Novonickname

    def elementos_magia (self,elemento_fogo,elemento_agua,elemento_ar,elemento_terra):
        self.elemento1 = elemento_agua
        self.elemento2 = elemento_fogo
        self.elemento3 = elemento_ar
        self.elemento4 = elemento_terra

    def get_elementos_magia(self):
        return self._magia

    def set_elementos_magia(self,nova_magia):
        self._magia = nova_magia

    def __str__ (self):
        return 'Meu nome é {}, sou o mais novo mago de Ventobravo. Sou um mago elementar de {}'.format(self._nickName,self._magia)

    def fraquezas(self, fraqueza_fogo, fraqueza_agua,fraqueza_terra,fraqueza_ar):
            self.elemento1 = fraqueza_fogo
            self.elemento2 = fraqueza_ar
            self.elemento3 = fraqueza_terra
            self.elemento4 = fraqueza_agua

jogador1 = Player()