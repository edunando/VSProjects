#Implemente uma lista encadeada seguindo os exemplos passados anteriormente(criando a classes Nó e ListaEncadeada)
# e faça um programa que junte duas listas
# dando origem a uma única lista com a terceira apontando seu primeiro elemento.

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

    def juntarlistas (self,lista1: 'ListaEncadeada', lista2: 'ListaEncadeada'):
        self.cabeca = lista1.cabeca
        lista1.cauda.prox = lista2.cabeca
        return 

    













''''''''''''''''''''''''''''     
lista1: 'ListaEncadeada' = ListaEncadeada()
lista1.inserir_valor_no_final(500)
lista1.inserir_valor_no_final(200)
lista1.inserir_valor_no_final(100)
lista1.inserir_valor_no_final(800)
lista1.inserir_valor_no_final(900)
lista2: 'ListaEncadeada' = ListaEncadeada()
lista2.inserir_valor_no_final(411)
lista2.inserir_valor_no_final(223)
lista2.inserir_valor_no_final(333)
lista2.inserir_valor_no_final(887)
lista2.inserir_valor_no_final(999)
lista3: 'ListaEncadeada' = ListaEncadeada()
lista3.juntarlistas(lista1,lista2)
lista3.imprimir_lista()
'''''''''''''''''''''''''''''''''  