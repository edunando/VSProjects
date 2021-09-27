        # LOCAL DAS FUNÇÕES
def divisores(n):
    resultado = [i for i in range(1, n + 1) if n % i == 0]
    return resultado


n = int(input('Insira o número para saber seus divisores: '))
print(f'Os divisores de {n} são: {divisores(n)}')