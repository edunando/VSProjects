print('BEM VINDO AO CONTADOR')
contador = ("Zero","Um","Dois","Três","Quatro","Cinco","Seis",
"Sete","Oito","Nove","Dez","Onze","Doze","Treze","Catorze","Quinze","Dezesseis","Dezessete","Dezoito","Dezenove","Vinte")
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if  0 <= num <= 20:
        print(f'Você Digitou o número: {contador[num]}')
        user=(input("Você quer Continuar? insira Y para continuar e N para encerrar o programa: "))
        if user == "N":
            print("Programa encerrado")
            break
    else:
        print('Você Digitou um número inválido.', end='' )
        user=(input("Você quer Continuar? insira Y para continuar e N para encerrar o programa: "))
        if user == "N":
            print("Programa encerrado")
            break

