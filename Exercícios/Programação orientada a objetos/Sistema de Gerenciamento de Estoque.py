class Produto:
    
    def __init__(self,nome, preço, quantidade_estoque):
        self.nome = nome
        self.preço = preço
        self.quantidade_estoque = quantidade_estoque

    
    def adicionar_estoque(self,):
        quantidade = int(input('Digite a quantidade: '))
        self.quantidade_estoque += quantidade
        print('Estoque atualizado.')
   
    
    def vender_produto(self):
        quantidade = int(input('Digite a quantidade: '))
        self.quantidade_estoque -= quantidade
        if self.quantidade_estoque < 0:
            print('Não foi possível concluir a venda.Quantidade indisponível em estoque')
            self.quantidade_estoque += quantidade
            print(f'Quantidade disponível: {self.quantidade_estoque}')
            self.vender_produto()
        else:
            print('Estoque atualizado.')


    def informaçoes(self):
        print('INFORMAÇÕES:')
        print('=============')
        print(f'Nome: {self.nome}')
        print(f'Preço: R${self.preço}')
        print(f'Quantidade: {self.quantidade_estoque}')


class Estoque:
    
    def __init__(self):
        self.produtos = []


    def adicionar_produtos(self,produto):
        self.produtos.append(produto)
        print(f'{produto.nome} adicionado ao estoque')    


    def mostrar_produtos(self):
        print("\n--- Produtos no Estoque ---")
        for produto in self.produtos:
            produto.informaçoes()

    def valor_total(self):
        total = sum(produto.preço * produto.quantidade_estoque for produto in self.produtos)
        print(f'O total é R${total: .2f}')        


produto1 = Produto("Celular", 1500.00, 10)
produto2 = Produto("Notebook", 3000.00, 5)
produto3 = Produto("Fone de Ouvido", 200.00, 50)
estoque = Estoque()

estoque.adicionar_produtos(produto1)
estoque.adicionar_produtos(produto2)
estoque.adicionar_produtos(produto3)

estoque.mostrar_produtos()
estoque.valor_total()




     

