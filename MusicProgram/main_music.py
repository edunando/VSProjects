from abc import *
from instrumentos import *
from Saxofone import *
from Violao import *
from Acordeon import *
from time import sleep
from musico import Musico


#EQUIPE: EDUARDO FERNANDO IVO CUNHA DA SILVA FILHO & BEATRIZ DE LIMA AMORIM
print('--' * 30)
print('SEJA BEM VINDO')
print('--' * 30)
sleep(1)

#dados dos Músicos
list_Instrumentos = ['Saxofone','Violao','Acordeon','Cavaquinho']
musico1 = Musico('Eduardo','Brasileiro')
musico2 = Musico('Ronaldinho','Brasileiro')
print('--' * 30)
print('Os Músicos que irão cantar hoje são:', musico1.nome)
print('Ele é', musico1.nacionalidade)
print('--' * 30)
sleep(3)
print('--' * 30)
print('e nosso outro convidado.... ',musico2.nome)
print('Ele também é ',musico2.nacionalidade)
print('--' * 30)
sleep(3)

#instrumentos
violao_eduardo = Violao('Elet Acústico','Palheta','Marrom','6 Cordas')
cavaquinho_eduardo = cavaquinho('Giannini','Palheta','Marrom','6 Cordas')
saxofone_ronaldinho = Sax('Duotar','Sopro','Dourado','baritono')
acordeon_ronaldinho = Acordeon('Todeschini','Sanfonado','Azul Marainho','120 Baixos','Estilo Clarinete')

#hora do show dos músicos
print('--' * 30)
print('PARA A APRESENTAÇÃO DE HOJE NOS TEMOS OS SEGUINTES INSTRUMENTOS...')
sleep(3)
Musico.exibirInstrumentos(Musico)
print('--' * 30)
sleep(5)
print('O Artista',musico1.nome,'é especialista em Violão e Cavaquinho e o artista',musico2.nome,'é mestre na arte do Acordeon e Saxofone' )
sleep(4)
adicione = 0

#escolha de músicos
while adicione != 5:
    print('--' * 30)
    try:
        adicione = int(input('Quem você deseja ouvir? Selecione \n (1) Eduardo \n (2) Ronaldinho\n (5) Encerrar Programa \n'))
    except ValueError: #Exceção caso ocorra um erro
        print('--' * 30)
        print('Valor inserido inválido. Insira um número.')
    print('--' * 30)
    sleep(3)
    if adicione == 1:
        print('HORA DO SHOW!!')
        print('Instrumento que será tocado é um Violão:',violao_eduardo.fabricante,violao_eduardo.tipo,violao_eduardo.cor,violao_eduardo.numCordas)
        print('E O Cavaquinho é um:',cavaquinho_eduardo.fabricante,cavaquinho_eduardo.tipo,cavaquinho_eduardo.cor,cavaquinho_eduardo.numCordas)
        sleep(5)
        print('--' * 30)
        print(musico1.nome,'Começa a se preparar')
        print('--' * 30)
        Violao.afinar(Violao)
        sleep(3)
        Violao.tocar(Violao)
        sleep(3)
        print('--' * 30)
        cavaquinho.afinar(cavaquinho)
        sleep(3)
        cavaquinho.tocar(cavaquinho)
        print('--' * 30)
        sleep(3)
    elif adicione == 2:
        print('HORA DO SHOW!!')
        print('Instrumento que será tocado é um Sax:',saxofone_ronaldinho.fabricante,saxofone_ronaldinho.tipo,saxofone_ronaldinho.cor,saxofone_ronaldinho.modelo)
        print('Junto com seu Acordeon:',acordeon_ronaldinho.fabricante,acordeon_ronaldinho.tipo,acordeon_ronaldinho.cor,acordeon_ronaldinho.numBaixo,acordeon_ronaldinho.numRegistros)
        sleep(5)
        print('--' * 30)
        print(musico2.nome,'Começa a se preparar')
        print('--' * 30)
        Acordeon.afinar(Acordeon)
        sleep(3)
        Acordeon.puxarFole(Acordeon)
        sleep(3)
        Acordeon.tocar(Acordeon)
        print('--' * 30)
        sleep(3)
        Sax.limpar(Sax)
        print('--' * 30)
        sleep(3)
        Sax.soprar(Sax)
        print('--' * 30)
        sleep(3)
        Sax.afinar(Sax)
        print('--' * 30)
        sleep(3)
        Sax.tocar(Sax)
        print('--' * 30)
        sleep(3)
    elif adicione == 5:
        print('Você Selecionou para encerrar o programa. Ficamos tristes com essa despedida. Até Logo....')
        break
    else:
        print('--' * 30)
        print('Como você inseriu uma opção inválida, vamos começar uma apresentação de demonstração com um Instrumento suspeito....') 
        print('--' * 30)
        sleep(4)
        print('--' * 30)
        print('Músico desconhecido se preparando pra tocar....')   
        print('--' * 30)
        sleep(3)
        musico1.iniciarDesmonstração()
        Instrumento.tocar(Instrumento)
        sleep(2)
        Instrumento.tocar(Instrumento)
        sleep(2)
        Instrumento.tocar(Instrumento)
        print('--' * 30)


