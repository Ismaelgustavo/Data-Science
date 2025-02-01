#  Adicione à classe Pessoa um método para alterar a idade e outro para verificar se a pessoa é maior de idade.

class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentaçao(self):
        print(f'Olá, Sou {self.nome} e tenho {self.idade} anos de idade')    

    def altera_idade(self,nova_idade):
        self.idade = nova_idade    

    def maioridade(self):
        if self.idade >= 18:
            print('Sou maior de idade')
        else:
            print('Sou menor de idade')    

      


pessoa = Pessoa('Ismael', 29)
Pessoa.altera_idade(pessoa, 45)
print(Pessoa.apresentaçao(pessoa))
Pessoa.maioridade(pessoa)


