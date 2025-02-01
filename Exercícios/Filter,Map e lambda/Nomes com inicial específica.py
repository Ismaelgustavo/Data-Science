'''
Dada uma lista de nomes e uma letra, filtre os nomes que começam com essa letra e transforme todos os nomes filtrados em letras minúsculas. Use um valor de letra predefinido no exercício, mas permita que o programa seja facilmente adaptável para outras letras.
'''
entrada = ["Alice", "Ana", "João", "Amanda", "Carlos"]
letra = 'C'
palavras_filtradas = []

def filtrando_nomes():
    
    for palavra in entrada:
        if palavra[0] == letra:
            palavras_filtradas.append(palavra)
    return palavras_filtradas        

print(list(map(lambda x: x.lower(), filtrando_nomes())))

