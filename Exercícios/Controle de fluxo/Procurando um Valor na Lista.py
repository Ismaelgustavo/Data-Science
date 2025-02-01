listaDeNumeros = [1, 4, 7, 9, 20, 23, 45, 169, 200, 274]

numeroDoUsuario = int(input('Digite um número: '))

for numero in listaDeNumeros:
        if numero == numeroDoUsuario:
            posicao = listaDeNumeros.index(numero) + 1
            print(f'O número {numeroDoUsuario} existe e está na posição {posicao} da lista')
            break

else:
        print('O número não existe na lista')        