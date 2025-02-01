jogador = {}

nome = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas jogou? '))
gols = []


for x in range (0, partidas):
    quantidade = input(f'Quantos gols na partida {x + 1}?')
    gols.append(quantidade)

jogador['nome'] = nome
jogador['partidas'] = partidas
jogador['gols'] = gols

print(jogador)
jogador['total'] = sum(gols)

for k,v in jogador.items():
    print(f'O campo {k} tem valor {v}')