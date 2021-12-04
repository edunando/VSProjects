class Aluno:
    def __init__ (self, n, i, m):
        self.nome = n
        self.idade = i 
        self.matricula = m

aluno1 = Aluno('Eduardo Fernando Ivo C. S. F.', 19, 20211380037)

print(f'O Nome do aluno é {aluno1.nome}')
print(f'O Aluno tem {aluno1.idade} anos.')
print(f'Matricula: {aluno1.matricula}')