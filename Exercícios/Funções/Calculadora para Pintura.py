largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
rendimentoLata = float(input('rendimento da lata de tinta:'))


def areaDaParede(largura, altura):
    area = largura * altura
    return float(area)


def calculoRendimento(area, rendimento):
    quantidadeLata = area / rendimento
    if quantidadeLata == 1:
        print(f'É necessária apenas {quantidadeLata} lata de tinta.')
    else:
        print(f'Serão necessárias {quantidadeLata: .2f} latas')    


area = areaDaParede(largura,altura)
calculoRendimento(area,rendimentoLata)

