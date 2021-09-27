entrada = input().split()
hora_inicial, hora_final = entrada
hora_inicial = int(entrada[0])
hora_final = int(entrada[1])


if hora_inicial < hora_final:
   duracao = hora_final - hora_inicial
else:
    duracao = (24 - hora_inicial) + hora_final
print("O JOGO DUROU",duracao,"HORA(S)") 