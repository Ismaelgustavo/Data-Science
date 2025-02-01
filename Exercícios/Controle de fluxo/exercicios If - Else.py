valor = float(input('Digite o valor: '))

desconto = (valor * 10) / 100

if valor > 100:
    print("Você tem um desconto de 10%")
    print(f'O valor a pagar é: R${valor - desconto}')

else:
    print('O valor a pagar é: R$', valor)    