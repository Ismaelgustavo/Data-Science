'''
Crie um dicionário com nomes como chaves e idades como valores.
Utilize sorted, lambda e dict para ordenar o dicionário por idade em ordem crescente.
'''

pessoas = {'ismael': 29, 'joão lucas': 22, 'vera': 52}

mais_velho = dict(sorted(pessoas.items(), key= lambda x: x[1] ))

print(mais_velho)