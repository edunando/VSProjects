
class No:
    def __init__(self, carga: object = None, prox: 'No' = None):
        self.carga = carga
        self.prox = prox
        
    def __str__(self):
        return str(self.carga)

class ListaEncadeada:
    def __init__(self):
        self.cabeca: 'No' = None
        self.cauda: 'No' = None
  
#INSERIR
    def inserir_valor_no_inicio(self, valor: object):
        novo:'No' = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo 
        else:
            novo.prox = self.cabeca
            self.cabeca = novo

    def inserir_valor_no_final(self, valor):
        novo = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo 
        else:
            self.cauda.prox = novo
            self.cauda = novo
#IMPRIMIR
    def imprimir_lista(self):
        if self.cabeca is None:
            print("Lista Vazia")
            return
        atual: 'No' = self.cabeca
        while atual is not None:
            print(str(atual.carga) + " ")
            atual = atual.prox
#REMOVER
    def remover_do_inicio(self):
      if self.cabeca is None:
          print("Lista vazia")
          return
      
      if self.cabeca == self.cauda:
          self.cabeca = self.cauda = None
      else:
          self.cabeca = self.cabeca.prox

    def remover_do_final(self): 
        if self.cabeca is None:
            print("Lista vazia")
            return
        
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            atual: 'No' = self.cabeca
            while atual.prox is not self.cauda:
                atual = atual.prox

            self.cauda = atual
            atual.prox = None

def extraiParesImpares(lista: 'ListaEncadeada'):
    pares = ListaEncadeada()
    impares = ListaEncadeada()
    atual: 'No' = lista.cabeca
    while atual is not None:
        if atual.carga  % 2 == 0:
                pares.inserir_valor_no_final(atual.carga)
        else:
                impares.inserir_valor_no_final(atual.carga)
        atual = atual.prox
    return pares, impares

inicio: 'ListaEncadeada' = ListaEncadeada()
inicio.inserir_valor_no_final(1)
inicio.inserir_valor_no_final(2)
inicio.inserir_valor_no_final(6)
inicio.inserir_valor_no_final(7)
inicio.inserir_valor_no_final(8)

pares, impares = extraiParesImpares(inicio)
print("Pares =")
pares.imprimir_lista()
print("Ímpares =")
impares.imprimir_lista()
