'''
Dada uma lista de números inteiros, filtre os números pares e calcule o quadrado de cada um deles. Retorne uma nova lista com os resultados.

'''

entrada = [1, 2, 3, 4, 5, 6]

pares = list(filter(lambda x: x % 2 == 0, entrada))

print(list(map(lambda x: x ** 2, pares)))