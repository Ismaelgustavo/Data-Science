'''
Dada a lista nomes = ["Ana", "Bruno", "Carla", "Daniel"], faça o seguinte:

Verifique se o nome "Carla" está na lista. Exiba uma mensagem confirmando se está ou não.
Substitua o nome "Bruno" por "Beatriz".
Remova o último elemento da lista.
Adicione o nome "Fernando" ao início da lista.

'''

nomes = ["Ana", "Bruno", "Carla", "Daniel"]

nome_buscado = "Ismael"

if nome_buscado in nomes:
    print('O Nome buscado exite na lista.')
else:
    print('O Nome buscado não se encontra na lista.')

nomes[1] = 'Beatriz'
print(nomes)

nomes.pop()
print(nomes)

nomes.insert(0, 'Fernando')
print(nomes)