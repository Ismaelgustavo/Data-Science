'''
Crie um dicionário que armazena produtos de uma loja:
Nome do produto como chave.
Outro dicionário com quantidade e preço como valores.
Escreva funções para:
Atualizar estoque.
Calcular o valor total de produtos em estoque.

'''

produtos = {

    'arroz': {
        'quantidade': 50,
        'preço': 1.50
    },
    'feijao': {
        'quantidade': 100,
        'preço': 2.00
    },
    'carne': {
        'quantidade': 150,
        'preço': 3.50
    }

}
opcao = 0


def atualiza_estoque():
    
    produto = str(input('Nome do produto: '))
    quantidade = int(input('quantidade : '))
    
    if produto in produtos:
        produtos[produto]['quantidade'] = quantidade
        print('Produto atualizado com sucesso.')


def calcula_estoque():
    total = 0
    for precos in produtos.values():
        total += precos['preço']
    return total    



while True:
    print('OPÇÕES')
    print('---------')
    print('1- Atualizar estoque')
    print('2- Valor total dos produtos')
    print('3- Encerrar programa')
    opcao = int(input('Digite a opção: '))
    
    if opcao == 1:
        atualiza_estoque()
    elif opcao == 2:
        print(f'O valor total contido em estoque é de R${calcula_estoque()}')
    elif opcao == 3:
        break    

