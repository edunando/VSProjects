Capital = float(input("Insira aqui seu capital:"))
Juros = float(input("Insira aqui o juros:"))
Periodo = int(input("Insira aqui o Período:"))

for i in range (0,Periodo):
    Capital = Capital + (Capital * Juros/100)

    print("O Seu valor é:",Capital,)
