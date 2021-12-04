frase = input("Insira uma frase: ")
vogal = "aeiou"
vogais_totais = 0
for v in frase:
    for frase in v:
        if frase.lower() in vogal:
           vogais_totais +=1
print(vogais_totais, 'vogais')