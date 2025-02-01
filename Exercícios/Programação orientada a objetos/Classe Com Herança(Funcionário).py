'''
Crie uma classe Funcionario que herda de Pessoa e adicione os atributos cargo e salario. Adicione um método para calcular o aumento do salário.
'''
 
class Pessoa:
    nome = 'ismael'
    idade = 30


class Funcionario(Pessoa):
    cargo ='Engenheiro'
    salario = 3000

    
    def Calculo_salario(self, aumento):
        self.salario += aumento
        print(f'O novo salário é no valor de R${self.salario}')


aumento = int(input('Digite o valor a ser acrescentado ao salário'))

pessoa1 = Funcionario()
Funcionario.Calculo_salario(pessoa1,aumento)
