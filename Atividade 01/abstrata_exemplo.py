from abc import ABC, abstractmethod

class Animal(ABC): # aqui, tem-se uma classe abstrata "Animal"

    def __init__(self, nome,tipo="terrestre"):
        self.nome = nome
        self.tipo = tipo
        
    @abstractmethod
    def atacar(self):
        pass

    def __str__(self):
        return f'Olá! Sou um {self.__class__.__name__}, um animal {self.tipo}'

class Gato(Animal):

    def __init__(self, nome, tipo="terrestre"):
        super().__init__(nome,tipo)
        
    def atacar(self):
        print('Se arma...encara...pula e arranha. ksssss kssss')

class Cachorro(Animal):

    #def __init__(self, nome, tipo="terrestre"):
     #   super().__init__(nome,tipo)
        
    def atacar(self):
        print('Rosna...olha na cara...mostra os dentes...baba e MORDE')
        

class Preguiça(Animal):
    def atacar(self):
        print('Não sei se estou com vontade.....')

class Peixe(Animal):
    def atacar(self, alvo="nenhum"):
        print('Nada pra esquerda, depois pra direita e MORDE')
        print('La se foi o ' + alvo)
        

    def nadar(self):
        print('Peixe esta nadando....')

# A instrução abaixo dá erro
#gato = Animal()

# Se instanciar um gato sem o método abstrato, vai dar erro
gato = Gato('xano')
print(gato)
gato.atacar()

cao = Cachorro('Sansão')
print(cao)
cao.atacar()


preguiça = Preguiça('Tonton')
print(preguiça)
preguiça.atacar()


print()
print('Observando o comportamento do PEIXE')
peixe = Peixe('Nemo','Aquatico')
print(peixe)
peixe.atacar()
peixe.nadar()


print()
print('Aplicando o POLIMORFISMO')
print('*' * 30)
for obj in [gato, cao, preguiça, peixe]:
    print(obj)
    obj.atacar()

'''    
    @abstractmethod
    def say_something(self): pass

class Cat(Animal):
    def say_something(self):
        return "Miauuu!" '''
