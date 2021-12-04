class FormaGeometrica:
    def __init__(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setNome(self,novoNome):
        self.nome = novoNome

    def calculaArea(self):
        return 0 # não calculará área

        # sem polimorfismo
    def areaFormaGeometrica(self):
        return 0

