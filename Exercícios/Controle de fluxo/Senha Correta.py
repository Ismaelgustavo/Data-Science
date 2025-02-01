# Definindo a senha correta
senha_correta = "1234"

# Inicializando uma variável para armazenar a entrada do usuário
senha_digitada = ""

# Loop que continua enquanto a senha digitada for diferente da correta
while senha_digitada != senha_correta:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada != senha_correta:
        print("Senha incorreta. Tente novamente.")

# Mensagem ao acertar a senha
print("Acesso permitido!")

