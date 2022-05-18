#!/bin/bash
#Aqui vou iniciar um 'laço de repetição' com o while true. o True significa que enquanto o programa não for interrompido pelousuário ele vai continuar rodando. Normalmente a gente interrompe o programa com o break.

#Inicio do laço
while true; do 
	read -p "Escolha uma Alternativa:" escolha #aqui vou pedir pro usuário escolher uma opção e armazenar na variável $escolha.
	case $escolha in #Inicio da estrutura do case com as opções
		"1") echo "Ray gosta de programação";;
		"2") echo "Ray adora programação";;
		"3") echo "Ray ama programação";;
		"4") echo "Ray vai me pagar um pastelzão";;
		"5") break;; #aqui é a opção para encerrar o While true
		*) echo "Você não selecionou uma opção válida :(";;
	esac #É Utilizado o case para iniciar e o esac para finalizar a estrutura do case
done #fim da estrutura do while
