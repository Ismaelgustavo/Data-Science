'''
Crie uma lista chamada valores com os seguintes números: 8, 3, 12, 5, 7, 1. Realize as operações abaixo:

Exiba a lista na ordem crescente.
Exiba a lista na ordem decrescente.
Inverta a ordem original da lista (não é ordem crescente ou decrescente, mas sim a inversão dos elementos).

'''

valores = [8, 3, 12, 5, 7, 1]
 
valores.sort()
print(valores)

valores.sort(reverse=True)
print(valores)

valores.reverse()
print(valores)
