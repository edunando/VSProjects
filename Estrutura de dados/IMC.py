from time import sleep

class IMCException(Exception):
    def imce(self):
        raise IMCException()

def imc(peso,altura):
    return peso / (altura * altura)

def main():
    print('--------------------')
    print('Calculadora IMC')
    print('--------------------')
    print('(c) calcular IMC')
    print('(s) Sair')
    print('(i) Para mais informações')
    print('---------------------')
    print()
    opcao = input('Selecione a opção: ')
    opcao = opcao.lower()
    while(True):
        if opcao == 'c': ### calcular IMC
            print('Olá , por favor preencha o formulário abaixo, para calcularmos o seu IMC!')
            tempo = sleep(0.6)
            try:
                massa = float(input('Digite o seu peso: '))
                altura = float(input('Digite a altura:').replace(',','.'))
                resultado = imc(massa,altura)
            except ValueError:
                print('Por favor, insira um NÚMERO válido.')
            else:
                print('Obrigado por preencher o formulário, agora iremos calcular o seu IMC para você!')
                tempo = sleep(0.6)
                print('Calculando...')
                sleep(1)
                try:
                    if resultado <= 18.05:
                                        print(f'Seu IMC é {resultado:.2f} Situação: Peso abaixo do normal. Neste caso, é necessária a busca por um especialista, para verificar a existência de algum problema de saúde causador do índice abaixo do normal;')
                    elif resultado >= 18.05 and resultado <= 24.09:
                                        print(f'Seu IMC é {resultado:.2f} Situação: São pesos considerados normais pela OMS;')
                    elif resultado >= 24.9 and resultado <= 29.9:
                                        print(f'Seu IMC é {resultado:.2f} Peso em pré-obesidade ou acima do peso, representando um risco maior para a saúde. Nesta causa, é imprescindível uma consulta com um especialista, pois pode estar relacionado à pressão alta, colesterol alto ou diabetes, podendo apontar até para o hipotireoidismo.')
                    elif resultado >= 29.9 and resultado <= 34.99:
                                        print(f'Seu IMC é {resultado:.2f} Situação: Este índice indica obesidade grau um. Este peso aumenta riscos para várias doenças, como diabetes, hipertensão arterial, o infarto do miocárdio e diversos tipos de câncer. A obesidade já é considerada uma comorbidade e necessita de tratamento profissional;')
                    elif resultado >= 34.9 and resultado <= 39.99:
                                       print(f'.Seu IMC é {resultado:.2f} Situação:Indica obesidade grau dois. Este peso já representa risco elevado para as doenças supracitadas.')                   
                    else:
                        raise IMCException()
                except IMCException as imce:
                            print('Situação: Seu IMC é igual ou maior do que o limite de 40.00. \n Indica obesidade grau três ou mórbida. O peso neste grau apresenta problemas extremamente graves e necessita de tratamento profissional com o máximo de recursos disponíveis, incluindo até cirurgia.')
                while(True):
                        escolher = input('(y) para continuar ou (n) voltar ao menu principal\nSelecione sua opção: ')
                        escolher = escolher.lower()
                        if escolher == 'n':
                            sleep(0.6)
                            print('--------------------')
                            print('Calculadora IMC')
                            print('--------------------')
                            print('(c) calcular IMC')
                            print('(s) Sair')
                            print('(i) Para mais informações')
                            print('---------------------')
                            print()
                            opcao = input('Selecione a opção: ')
                            opcao = opcao.lower()
                            break
                        if escolher == 'y':
                                print('OK, Vamos continuar.')
                                sleep(0.6)
                                break
                        else: 
                            sleep(0.6)
                            print('--------------------')
                            print('por favor escolha um dos valores apresentados')
                            print('--------------------')
                            sleep(0.6)
        elif opcao == 'i':
                print('\nVocê já se perguntou se você é uma pessoa saudável? Estou aqui para lhe ajudar. \nO IMC é reconhecido como padrão internacional para avaliar o grau de sobrepeso e obesidade. É calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).No entanto, não mede diretamente a gordura corporal, pois não contempla a estrutura óssea, massa magra, massa gorda e líquidos. A importância de estar dentro do peso ideal está diretamente ligada ao estado de saúde.')
                sleep(5)
                print('--------------------')
                print('Calculadora IMC')
                print('--------------------')
                print('(c) calcular IMC')
                print('(s) Sair')
                print('(i) Para mais informações')
                print('---------------------')
                print()
                opcao = input('Selecione a opção: ')
                opcao = opcao.lower()
        elif opcao == 's':
                print('Programa finalizado')
                break
        else:
                print('POR FAVOR INSIRA UM DOS VALORES APRESENTADOS.')
                print('--------------------')
                print('Calculadora IMC')
                print('--------------------')
                print('(c) calcular IMC')
                print('(s) Sair')
                print('(i) Para mais informações')
                print('---------------------')
                print()
                opcao = input('Selecione a opção: ')
                opcao = opcao.lower()
        
if __name__ == '__main__':
    main()