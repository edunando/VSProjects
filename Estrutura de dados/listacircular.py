from ListaEncadeada import No

class ListaCircular:

    def __init__(self):
        self.cabeca = None
        self.cauda = None 
        self.total = 0
       
    def imprimir_lista(self):
        if self.cabeca is None:
            print("Lista vazia")
            return

        atual: 'No' = self.cabeca
        print(atual)
        
        while atual is not self.cauda: 
            print(atual.prox)
            atual = atual.prox


    def inserir_no_inicio(self, valor: object):
        novo: 'No' = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:        
            novo.prox = self.cabeca
            self.cabeca = novo
            novo.prox.ant = novo
            self.cabeca.ant = self.cauda
            self.cauda.prox = self.cabeca 

    def inserir_no_final(self, valor):
        novo: 'No' = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:
          novo.ant = self.cauda 
          novo.ant.prox = novo 
          self.cauda = novo 
          self.cauda.prox = self.cabeca 
          self.cabeca.ant = self.cauda 


    def remover_do_inicio(self):
        if self.cabeca is None:
            print("Lista vazia")
            return
        
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.prox 
            self.cabeca.ant = self.cauda 
            self.cauda.prox = self.cabeca 

    def remover_do_final(self):
        if self.cabeca is None:
            print("Lista vazia")
            return
        
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cauda = self.cauda.ant
            self.cauda.prox = self.cabeca 

    def __len__(self):
        atual = self.cabeca
        if self.cabeca is not None:
            self.total += 1
        while atual is not self.cauda:
            self.total += 1
            atual = atual.prox
        print('Elementos da lista:',self.total)

lista: 'ListaCircular' = ListaCircular()
lista.inserir_no_final(100)
lista.inserir_no_final(200)
lista.inserir_no_final(300)
lista.inserir_no_final(400)
lista.remover_do_inicio()
lista.remover_do_final()
lista.inserir_no_inicio(800)
lista.inserir_no_final(2)
lista.inserir_no_final(8)
lista.inserir_no_final(0)
lista.imprimir_lista()
lista.__len__()