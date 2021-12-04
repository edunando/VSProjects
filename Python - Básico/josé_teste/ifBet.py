import funcoes
import random

quantidadeJogadores = int(input('Digite a quantidade de jogadores: '))
listaCartelas = []
numerosSorteados = []
vencedor = False

for i in range(quantidadeJogadores):
    listaCartelas.append(funcoes.novo(1, 10))

while vencedor == False:
    numeroSorteado = random.randint(1, 10)
    print('Número sorteado: {}'.format(numeroSorteado))
    funcoes.inserir(numeroSorteado, numerosSorteados)
    
    for k in range(len(listaCartelas)):
        print(str(listaCartelas[k]) + ' ' + str(funcoes.verificar(listaCartelas[k], numerosSorteados)))

    for j in range(quantidadeJogadores):
        if funcoes.verificar(listaCartelas[j], numerosSorteados) == 6:
            print('Vencedor: Cartela ' + str(j + 1))
            vencedor = True
            break
        
    if vencedor == False:
        print('Ainda não temos um vencedor')
        input('Aperte <Enter>')
    
    
    
