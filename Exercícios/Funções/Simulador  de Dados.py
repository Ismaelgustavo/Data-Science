import random

valor_dados = []

def simulador_dados():
    valor = random.randint(1, 5+1)
    print(valor)
    return valor
    

for x in range(2):
    dado_um = valor_dados.append(simulador_dados())

soma = sum(valor_dados) 
print(soma)