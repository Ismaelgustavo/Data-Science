'''
Crie uma lista chamada numeros com os valores 1, 2, 3, 4 e 5. Faça as seguintes operações:

Multiplique cada elemento da lista por 2 e armazene os resultados em uma nova lista chamada dobros.
Exiba a lista dobros na tela.

'''

numeros = [1, 2, 3, 4 , 5]
dobros = []

for x in numeros:
    multiplicador = x * 2
    dobros.append(multiplicador)

print(dobros)    