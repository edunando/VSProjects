from funçoes_2 import novo,contido,verificar,inserir
#sorteio
v1 = int(input('Valor mínimo a ser gerado: '))
v2 = int(input('Valor máximo a ser gerado: '))
print()
print(f'Os números gerados entre {v1} e {v2} foram:',novo(v1,v2))
print()
#contido
list_ = list(range(0,50 +1))
numeral = int(input('Qual número você quer checar se está na lista?: '))
print()
contido(numeral,list_)
print()
#verificar
lista2 = list(range(32,91))
print('Checando valores das duas listas...')
print()
verificar(list_,lista2)
#inserir
print()
inserir_num = int(input('Insina o número:'))
inserir(inserir_num,list_)    