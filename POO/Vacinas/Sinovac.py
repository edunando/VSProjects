class Sinovac:
  __LABORATORIO = 'Sinovac BioTech'
  def __init__(self, nDoses , intervalo, tecnologia, voluntários ):
    self.__numDoses = nDoses
    self.__intervalo = intervalo # intervalo mínimo para a próxima dose
    self.__aprovada = False
    self.__preço = 0.0 # preço por dose
    self.__voluntários = voluntários #voluntários em ensaios clínicos no Brasil
    self.__tecnologia = tecnologia

  @property
  def voluntários(self):
    return self.__voluntários

  @voluntários.setter
  def volutários(self, novaNumero):
    self.__voluntários = novoNumero

  @property
  def intervalo(self):
    return self.__intervalo

  @intervalo.setter
  def intervalo(self, novoIntervalo):
    self.__intervalo = novoIntervalo

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
    assert novoPreço >= 0
    return self.__preço

  @preço.setter
  def preço(self, novoPreço):
    self.__preço = novoPreço

  def country(self):
    return 'China'

  @classmethod
  def laboratorio(cls):
    return cls.__LABORATORIO

  def __str__(self):
    return f'''
Vacina {Sinovac.__name__}, 
Laboratório: {Sinovac.__LABORATORIO}, 
Numero de Doses = {self.numDoses}, 
Tecnologia: {self.__tecnologia},
Intervalo mínimo para aplicação da próxima dose: {self.__intervalo}, 
Voluntários nos ensaios clínicos (BR): {self.__voluntários}'''
