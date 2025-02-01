vendas = {
    "Janeiro": 1500,
    "Fevereiro": 2000,
    "Março": 1700
}
lista_Vendas = []

def total_vendas():
    total = 0

    for venda in vendas.values():
        total += venda
    
    return total    


def vendas_mensais():
    
    maior_mes = max(vendas, key=vendas.get)
    menor_mes = min(vendas, key=vendas.get)

    print(f'O mês que mais vendeu é o mês de {maior_mes}')
    print(f'O de menor vendas é {menor_mes}')
    

print(total_vendas())
vendas_mensais()