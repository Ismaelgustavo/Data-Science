# Peça um número ao usuário e faça uma contagem regressiva até 0. Ao final, imprima "Lançamento!"

numero = int(input('Digite um número: '))

while numero >= 0:
    print(numero)
    numero -= 1

print('LANÇAMENTO')    
   