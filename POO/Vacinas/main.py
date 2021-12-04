from Vacinas import classOMS, Janssen, Oxford, Sinovac
 
o = Oxford(2, 14, 'Vetor Viral (adenovirus)', 77)
o.aprovada = True
print(o)
print()

s = Sinovac(2,20, 'Virus inativado (morto)', 12000)
s.aprovada = True
print(s)
print()

j = Janssen(1,'Vetor Viral (adenovirus)','De 2 a 8 graus Celcius')
j.aprovada = True
print(j)



oms = OMS()
oms.cadastrarVacina(o)
oms.cadastrarVacina(s)
oms.cadastrarVacina(j)

print('\n\nListagem por polimorfismo')
print('--------------------------')
oms.listarVacinasAprovadas()