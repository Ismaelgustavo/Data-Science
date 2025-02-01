'''
Crie um dicionário onde as chaves são nomes de produtos e os valores são seus preços.
Escreva uma função chamada aplicar_desconto() que recebe o dicionário e um valor de desconto (em porcentagem) e retorna um novo dicionário com os preços atualizados.

'''

produtos = {

    'Celular': 1300,
    'Airfrayer': 200,
    'tablet': 500

}
tabela_desconto = {}
desconto = 0


def calcula_desconto(valor_desconto):
    
    desconto = 0
    for produto,preço in produtos.items():
        desconto = preço * (valor_desconto/100)
        tabela_desconto[produto] = desconto + preço

desconto = int(input('Digite o valor do desconto: '))

calcula_desconto(desconto)

print(f'A nova tabela de preços com o desconto de {desconto}% é:')

for produto,valor in tabela_desconto.items():
    print(f'{produto}: R${valor: .2f}')
    print('_____________________')

    

