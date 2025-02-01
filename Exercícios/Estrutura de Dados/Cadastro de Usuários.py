'''
Escreva um programa que usa um dicionário para armazenar informações de usuários. Cada chave do dicionário será o nome do usuário, e o valor será outro dicionário com as informações:
Idade
E-mail
Permita que o usuário adicione novos registros ao dicionário.

'''

usuario = {}

def cria_usuario(usuario):
    nome = str(input('Nome: '))

    if nome in usuario:
            print(f"O usuário '{nome}' já existe!")
            return

    idade = int(input('Idade: '))
    email = str(input('E-mail: '))

    usuario[nome] = {

        'idade': idade,
        'email': email

    }
    

    print(f'Usuário {nome} adicionado com sucesso')
    


def consulta_usuario():
     
    global usuario
    if not usuario:
        print("Nenhum usuário cadastrado.\n")
        return
    
    print('=-=-=-=-=-=-=-=-=-=-=')
    print("Usuários cadastrados:")

    for nome, dados in usuario.items():
        
        print(f"Nome: {nome}")
        print(f"  Idade: {dados['idade']}")
        print(f"  E-mail: {dados['email']}\n")
            




while True:
    print("1. Adicionar usuário")
    print("2. Exibir usuários")
    print("3. Sair")
    
    opcao = int(input('Digite a opção: '))
    
    if opcao == 1:
        cria_usuario(usuario)

    elif opcao == 2:
        consulta_usuario()   

    elif opcao == 3:
        break
