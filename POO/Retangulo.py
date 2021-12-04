class Retangulo:
    def __init__(self,b,a):
        self.base = b
        self.altura = a

    def calcula_area(self):
        return self.base * self.altura

rect = Retangulo(1.34,5.2)
print(rect.calcula_area())
print(rect.base)
print(rect.altura)