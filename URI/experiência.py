quant = int(input())
quant_total = 0
quant_r = 0
quant_c = 0
quant_s = 0

for i in range(quant):
    valores = input().split()
    quantia, tipo = valores
    quant_total += int(quantia)
    
    if(tipo == "C"):
        quant_c += int(quantia)
    else:
        if(tipo == "R"):
            quant_r += int(quantia)
        else:
            quant_s += int(quantia)

print("Total: %d cobaias" %quant_total)
print("Total de coelhos: %d" %quant_c)
print("Total de ratos: %d" %quant_r)
print("Total de sapos: %d" %quant_s)
print("Percentual de coelhos: {:.2f} %".format((quant_c/float(quant_total))*100))
print("Percentual de ratos: {:.2f} %".format((quant_r/float(quant_total))*100))
print("Percentual de sapos: {:.2f} %".format((quant_s/float(quant_total))*100))