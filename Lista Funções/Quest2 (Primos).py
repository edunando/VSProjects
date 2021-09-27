def primo(n):
    resultado = [i for i in range(1, n + 1) if n % i == 0]
    return resultado

n = int(input('Insira o número para saber se é primo: '))
if primo(n)[1] == n:
    print('É primo')
else:
    print('Não é primo')
    print(primo(n))
