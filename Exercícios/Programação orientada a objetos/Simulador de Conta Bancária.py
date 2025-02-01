class Cliente:
    nome = 'Ismael'
    numero_conta = 13431114636
    saldo = 0
    senha = 1234

    def depositar(self, valor):
        self.saldo = valor

    def sacar(self, valor):
        self.saldo -= valor

    def exibir_saldo(self):
        print(f'Seu saldo é de R${self.saldo: .2f}')


def valida_senha():
    senha = int(input('Digite sua senha: '))
    if senha != Cliente.senha:
        valida_senha()          
    else:
        return        

def login_cliente():
    print('-=-=-=-=-=-=-=-=-=-')
    conta = int(input('Digite o nº da sua conta: '))
    if conta != Cliente.numero_conta:
        print('Numero errado')
        login_cliente()
    else:
        valida_senha()




while True:
        login_cliente()
        

        print('=================')
        print('1- Depósito')
        print('2- Saque')
        print('3- Saldo')
        print('4- Sair')
        opçao = int(input('Digite sua opção: '))
        if opçao == 1:
            valor = int(input('Valor: '))
            Cliente.depositar(Cliente, valor)
            print('Valor Depositado')
            
            
        elif opçao == 2:
            valor = int(input('Valor: '))
            Cliente.sacar(Cliente, valor)
            print(Cliente.saldo)
            print('Saque Concluído')

        elif opçao == 3:
            Cliente.exibir_saldo(Cliente)
            break

        elif opçao == 4:
            print('Obrigado! Volte Sempre.')
            break



    



        
    





        