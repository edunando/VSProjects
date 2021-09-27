N = int(input())

minutos = int(N/60);
N -= minutos*60;
horas = int(minutos/60);
minutos -= horas*60;

print(repr(horas)+":"+repr(minutos)+":"+repr(N))