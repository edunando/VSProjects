class Janssen:
  __LABORATORIO = 'Johnson & Johnson'
  def __init__(self, nDoses , tecnologia, armazenamento ):
    self.__numDoses = nDoses
    self.__aprovada = False
    self.__preço = 0.0 # preço por dose
    self.__armazenamento = armazenamento
    self.__tecnologia = tecnologia

  @property
  def armazenamento(self):
    return self.__armazenamento

  @armazenamento.setter
  def armazenamento(self, novoArmazenamento):
    self.__armazenamento = novoArmazenamento

  @property
  def numDoses(self):
    return self.__numDoses

  @property
  def aprovada(self):
    return self.__aprovada

  @aprovada.setter
  def aprovada(self, status):
    self.__aprovada = status

  @property
  def preço(self):
    return self.__preço

  @preço.setter
  def preço(self, novoPreço):
    assert novoPreço >= 0
    self.__preço = novoPreço

  def country(self):
    return 'USA'

  @classmethod
  def laboratorio(cls):
    return cls.__LABORATORIO

  def __str__(self):
    return f'''
Vacina {Janssen.__name__}, 
Laboratório: {Janssen.__LABORATORIO}, 
Numero de Doses = {self.numDoses}, 
Tecnologia: {self.__tecnologia}, 
Armazenamento: {self.__armazenamento}'''

