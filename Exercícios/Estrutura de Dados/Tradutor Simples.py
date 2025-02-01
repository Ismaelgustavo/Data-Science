palavras = {

    'sol': 'sun',
    'cor': 'color',
    'água':'water'

}


def traduçao(palavra):
    palavra_traduzida = ''

    if palavra in palavras:
        palavra_traduzida = palavras[palavra]
        return str(palavra_traduzida)


palavra = str(input('Digite a palavra: '))
print(f'Essa Palavra em inglês é {traduçao(palavra)}')

