'''
Crie um sistema para gerenciar o estoque de uma loja usando dicionários:
Cada chave representa o nome do produto.
O valor associado a cada chave é outro dicionário com:
Preço do produto.
Quantidade em estoque.
Crie funções para:
Adicionar novos produtos.
Atualizar o estoque de um produto.
Consultar o preço de um produto.

'''

produtos = {}



def adiciona_produto():

    nome_produto = str(input('Nome: '))
    preço = float(input('Preço do Produto: '))
    quantidade = int(input('Quantidade em estoque: '))

    produtos[nome_produto] = {
        
        'preço': preço,
        'quantidade': quantidade

    }
    print('=-=-=-=-=-=-=-=-')
    print('PRODUTO ADICIONADO')
    print('=---=-=-=-=-=-=-')


def atualiza_estoque():

    nome_produto = str(input('Nome: '))
    quantidade = int(input('Quantidade em estoque: '))
    
    if nome_produto in produtos:
        produtos[nome_produto]['quantidade'] = quantidade
        print(produtos)


def consultar_preço():

    nome_produto = str(input('Nome: '))
    
    if nome_produto in produtos:
        
        print(f'O preço do produto {nome_produto} é R$:{produtos[nome_produto]['preço']}')


def lista_produtos():

    for produto, dados in produtos.items():
        print(f'`{produto}: está custando R${dados['preço']} e tem {dados['quantidade']} armazenados em estoque')



while True:
    
    print('1- Adicionar novos produtos.')
    print('2- Atualizar o estoque de um produto.')
    print('3- Consultar o preço de um produto.')
    print('4- finalizar programa')

    opçao = int(input('Digite a opção: ')) 

    if opçao == 1:
        adiciona_produto()
    
    elif opçao == 2:
        atualiza_estoque()

    elif opçao == 3:
        consultar_preço()

    elif opçao == 4:
        lista_produtos()
        break    












