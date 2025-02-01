# Peça ao usuário dois números A e B (onde A < B). Mostre todos os números pares no intervalo [A, B].

primeiroNumero = int(input('Digite um número: '))
segundoNumero = int(input('Digite mais um número: '))
conjuntoNumeros = []
numeroMaior = 0
numeroMenor = 0

if primeiroNumero > segundoNumero:
    numeroMaior = primeiroNumero
    numeroMenor = segundoNumero
else:
    numeroMaior = segundoNumero
    numeroMenor = primeiroNumero

for x in range(numeroMenor, numeroMaior + 1):
    resto = x % 2
    if resto == 0:
        conjuntoNumeros.append(x)
        print(x)