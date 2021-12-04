from random import randint
from bingo1 import novo
from bingo1 import verificar
from bingo1 import inserir
from bingo1 import contido
from bingo1 import limpar
limpar()
print('IFBET')
print()
lista_cartelas = []
numeros_sorted = []
cartelas_vencedoras = []
cont = 0
jogadores_quant = int(input('Insira a quantidade de jogadores: '))
for i in range (jogadores_quant):
    cartelas = novo(1,10)
    inserir(cartelas,lista_cartelas)
print()
while True:
    numero_sorteado = randint(1,10)
    print('número sorteado', numero_sorteado)
    if not contido(numero_sorteado, numeros_sorted):
        inserir(numero_sorteado, numeros_sorted)
        cont += 1
    for i in range(len(lista_cartelas)):
        print(str(lista_cartelas[i]) + ' ' + str(verificar(lista_cartelas[i],numeros_sorted)))
    for cartela in (lista_cartelas):
        if verificar(cartela, numeros_sorted) == 6 and not contido(cartela,cartelas_vencedoras):
            cartelas_vencedoras.append(cartela)
            print('cartelas vencedoras', cartelas_vencedoras)
            break
    input('Ainda não houve vencedores\n Pressione qualquer tecla para continuar')
    limpar()
