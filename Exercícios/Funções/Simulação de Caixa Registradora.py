'''
Escreva um programa com funções:
Uma função adicionar_item(preco) que adiciona o preço de um item ao total da compra.
Uma função exibir_total() que mostra o total acumulado até o momento.
Uma variável global total deve armazenar o valor acumulado.


'''

total = 0

def adicionar_item():
    global total
    continua_compra = True


    while continua_compra:
        preço_item = float(input('Digite o preço da compra:  '))
        total += preço_item
        print(total)
        exibir_total()
        print('Deseja adicionar mais preços ao total da compra?')
        print('S para sim ou não para N para mostrar o total')
        resposta = input()

        if resposta == 'n' or resposta == 'N':
             continua_compra = False
             exibir_total()


def exibir_total():
    global total
    print(f'O total da compra é {total: .2f}')

adicionar_item()


