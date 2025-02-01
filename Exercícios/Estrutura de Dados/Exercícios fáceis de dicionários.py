'''
Criação de Dicionário Simples:

Crie um dicionário chamado aluno com as seguintes informações:
Nome: "João"
Idade: 20
Curso: "Engenharia"
Imprima o nome e o curso do aluno.

'''

# aluno = {'Nome':'João', 'Idade':20, 'Curso': 'Engenharia' }

#print(aluno['Nome'], aluno['Curso'])

produto = {
    "nome": "Camiseta",
    "preço": 29.99,
    "quantidade": 10
}

chave_desconto = "desconto"

# Verifica se a chave 'desconto' já existe
if chave_desconto not in produto:
    produto[chave_desconto] = 0

print(produto)

