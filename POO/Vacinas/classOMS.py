class OMS:
  def __init__(self):
    self.__vacinas = []

  def cadastrarVacina(self, vacina):
    self.__vacinas.append (vacina)

  @property
  def vacinas(self):
    return self__vacinas

  def listarVacinasAprovadas(self):
    ###############################
    # IMPLEMENTAR COM POLIMORFISMO
    ###############################
    print('Implementar com polimorfismo')