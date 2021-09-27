tabela = ('Atlético-MG','Palmeiras','Fortaleza','Bragantino','Flamengo','Corinthians','Atlético-GO','Ceará SC','Cuiabá','Atletico-PR','Internacional','Fluminense',
'Santos','Juventude','São Paulo','Bahia','América-MG','Grêmio','Sport Recife','Chapecoense')

print("TABELA BRASILEIRÃO SÉRIA A 2021")
for i in range (0,5):
    print(f'Os cinco primeiros colocados são: {tabela[i]} em {i+1} º lugar.')

for j in range(16,19): 
    print(f'Os 4 últimos colocados atuais são: {tabela[j]} em {j+1} º lugar.')

x= sorted(tabela)
print('Os times atuais Ordenados são:',x)

print('O Chapecoense está na ', tabela.index('Chapecoense')+1,'º','posição')