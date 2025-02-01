'''
Dada uma lista de números inteiros, filtre os números ímpares e eleve-os ao cubo. Depois, calcule a soma de todos esses números elevados ao cubo.

'''

entrada = [1, 2, 3, 4, 5]

impares = list(filter(lambda x: (x % 2 != 0) ** 3 , entrada))
ao_cubo = list(map(lambda x:x ** 3, impares))

print(sum(ao_cubo))




