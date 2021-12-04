import csv
from typing import List

def carrega_servidores_DNS():
  servidores_dns = []
  with open('dns_br.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=';')
      next(csv_reader, None)  # pula os cabeçalhos
      for row in csv_reader:
          servidor_dns = dict()
          servidor_dns['ip'] = row[0]
          servidor_dns['nome'] = row[1]
          servidores_dns.append(servidor_dns)
  return servidores_dns

def busca_linear_recursiva(nome: str, servs: List[dict]) -> str:
  if len(servs) == 0 or nome < servs[0]['nome']:
    return ""
  if nome == servs[0]['nome']:
    return servs[0]['ip']
  servs.pop(0)
  return busca_linear_recursiva(nome,servs)
   
def busca_binaria(nome: str, servidores_dns: List[dict]) -> str:
  primeiro = 0
  ultimo = len(servidores_dns)-1
  while primeiro <= ultimo:
    meio = (primeiro+ultimo) // 2
    if servidores_dns[meio][nome] == nome:
      return servidores_dns[meio]['ip']

    if nome < servidores_dns[meio]['nome']:
      ultimo = meio - 1
    else:
      primeiro = meio + 1
  return ""







if __name__ == '__main__':
    servidores_dns = carrega_servidores_DNS()
    servidores_dns.sort(key=lambda d: d['nome'])
    print('Busca Linear Recursiva: ')
    resultado = busca_linear_recursiva('CENTROSULNET INFORMATICA EIRELI',servidores_dns.copy())
    print(resultado)