# Peça ao usuário uma lista de números e encontre o maior valor presente nela.
conjuntoNumeros = []

for x in range(1,10 + 1):
    print('Digite 10 números aleatórios que descobrirei o maior.')
    numero = int(input(f'numero { x }: '))
    conjuntoNumeros.append(numero)
    
print(max(conjuntoNumeros))

