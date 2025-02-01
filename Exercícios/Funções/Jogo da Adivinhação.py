import  random

numero = 0
palpite = 0


def jogo_adivinhaçao():
    global numero,palpite
    palpite = int(input('Digite um número: '))

    if palpite > numero:
            print('Palpite acima do valor!')
            print(numero)
            jogo_adivinhaçao()
    elif palpite < numero:
            print('Palpite muito abaixo do valor!')
            print(numero)
            jogo_adivinhaçao()
    else:
        print(f'Parabéns!!!Você acertou o número: {numero}')
        
            
                

        

numero = random.randint(1,100+1)
jogo_adivinhaçao()




