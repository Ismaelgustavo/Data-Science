'''
Dado um dicionário de produtos com seus preços, filtre apenas os produtos cujo preço seja maior que 50 e aplique um desconto de 10%. Retorne uma nova lista com os preços atualizados.

'''

produtos = {"Celular": 1500, "Cabo USB": 25, "Monitor": 750, "Mouse": 45, "Teclado": 120}

maior_50 = dict(filter(lambda x: x[1] > 50, produtos.items()))
preços = list(maior_50.values())

desconto = list(map(lambda x: x - ((x * 10) / 100), preços))
print(desconto)

