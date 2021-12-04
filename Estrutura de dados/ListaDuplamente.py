from ListaEncadeada import *
class No:
    def __init__(self, carga: object = None, 
                 ant: 'No' = None,
                 prox: 'No' = None):
        self.carga = carga
        self.prox = prox
        self.ant = ant

    def __str__(self):
        return str(self.carga)
class ListaDuplamenteEncadeada(ListaEncadeada): # herdamos da classe ListaEncadeada para reaproveitar o método imprimir_lista
    def __init__(self):
        self.cabeca = None
        self.cauda = None  

    def inserir_no_final(self, valor):
        novo: 'No' = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:
            novo.ant = self.cauda 
            novo.ant.prox = novo 
            self.cauda = novo 

  #### Resposta ####

  # O método remover_por_valor só remove a primeira ocorrência, é preciso garantir que todas sejam removidas  
    def remover_por_valor(self, valor):
        if self.cabeca is None:
            ...
        if self.cabeca is not None:
            ant = None
            atual = self.cabeca
            while atual is not None:
                if atual.carga == valor:
                    if ant is None:
                        self.cabeca = atual.prox
                        return
                    else:
                        ant.prox = atual.prox
                        return
                ant = atual
                atual = atual.prox

    def remover_ocorrencias(self,valor):
        if self.cabeca is None:
                ...
        if self.cabeca is not None:
            atual = self.cabeca
            atual.prox = atual
            while atual is not None:
                if atual.carga == valor:
                    self.remover_por_valor(atual.carga)
                break

lista: 'ListaDuplamenteEncadeada' = ListaDuplamenteEncadeada()
lista.inserir_no_final(10)
lista.inserir_no_final(10)
lista.inserir_no_final(10)
lista.inserir_no_final(50)
lista.inserir_no_final(10)
lista.inserir_no_final(10)
lista.remover_ocorrencias(10)
lista.imprimir_lista()