elementos = int(input())
valores = []
valores = list(map(int,input().split()))
print('Menor valor:',min(valores))
print('Posicao:',valores.index(min(valores)))

#O list foi usado pelo fato de ser uma lista, o mapodemos usar a função integrada do Python, map(), para aplicar uma função a cada item em um iterável 
# (como uma lista ou um dicionário) e retornar um novo iterador para recuperar os resultados. map() retorna um objeto map (um iterador), que podemos usar 
# em outras partes do nosso programa. O index para retornar a posição da variavel na lista e o min para retornar o valor minimo da lista.
#A sintaxe para a função map() é a seguinte:
# map(function, iterable, [iterable 2, iterable 3, ...])
#
#