class Oxford:
  __LABORATORIO = 'AstraZeneca'
  def __init__(self, nDoses , intervalo, tecnologia, eficacia  ):
    self.__numDoses = nDoses
    self.__intervalo = intervalo # intervalo mínimo para aplicar a próxima dose
    self.__aprovada = False
    self.__preço = 0.0 # preço por dose
    self.__eficaciaGlobal = eficacia # após as n doses
    self.__tecnologia = tecnologia # tecnologia por trás da produção da vacina

  @property
  def numDoses(self):
    return self.__numDoses

  @property
  def intervalo(self):
    return self.__intervalo

  @intervalo.setter
  def intervalo(self, novoIntervalo):
    self.__intervalo = novoIntervalo

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
    return 'England'

  @classmethod
  def laboratorio(cls):
    return cls.__LABORATORIO

  def __str__(self):
    return f'''
Vacina {Oxford.__name__}, 
Laboratório: {Oxford.__LABORATORIO}, 
Numero de Doses = {self.numDoses}, 
Tecnologia: {self.__tecnologia}, 
Intervalo mínimo para aplicação da próxima dose: {self.__intervalo}, 
Eficacia: {self.__eficaciaGlobal}%'''

