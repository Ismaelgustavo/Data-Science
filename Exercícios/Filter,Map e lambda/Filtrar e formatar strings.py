'''
Dada uma lista de strings, filtre apenas as strings que têm mais de 5 caracteres e converta todas as letras para maiúsculas. Retorne uma nova lista com as strings formatadas.

'''

entrada = ["python", "map", "filter", "lambda", "list", "code"]

cinco_caracteres = list(filter(lambda x: len(x) > 5 , entrada))

print(list(map(lambda x: x.upper(), cinco_caracteres)))