'''
Crie uma lista chamada meus_numeros que contenha os números: 10, 20, 30, 40, 50. Realize as seguintes operações:

Adicione o número 60 ao final da lista.
Insira o número 15 na segunda posição.
Remova o número 40 da lista.
Exiba a lista final na tela.

'''

meus_numeros = [10, 20, 30, 40, 50]

meus_numeros.append(60)
meus_numeros.insert(1, 15)
meus_numeros.remove(40)
print(meus_numeros)