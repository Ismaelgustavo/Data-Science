import random
print('-=-=-=-=-=-=-=-=-=-=-=-=-')
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-=-=-=-=-=-=-=-=-=-=-=-')
valor = int(input('Diga um valor: '))
par_impar = str(input('Par ou Ìmpar?  [P/I] '))
    
valor_computador = random.randint(0, 11) 
conta_vitorias = 0



def inicia_jogo():
    global valor, par_impar
    print('-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('VOCE VENCEU VAMOS JOGAR NOVAMENTE')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-')
    valor = int(input('Diga um valor: '))
    par_impar = str(input('Par ou Ìmpar?  [P/I] '))
    

def par_impar_(valor):
    if valor == 'I' or valor == 'i':
        return 'IMPAR'
    
    elif valor == 'P' or valor == 'p':
        return 'PAR'



def par_impar_Computador(valor):
    if valor % 2 != 0:
        return 'IMPAR'
    
    else:
        return 'PAR'



while True:
    resultado = valor + valor_computador
    if resultado % 2 == 0 and par_impar_(par_impar) == 'PAR':
        print(f'Voce jogou {valor} e o computador jogou {valor_computador}. Total deu {resultado} é {par_impar_(par_impar)}')
        conta_vitorias += 1
        inicia_jogo()
        

    elif resultado % 2 != 0 and par_impar_(par_impar) == 'IMPAR':
        print(f'Voce jogou {valor} e o computador jogou {valor_computador}. Total deu {resultado} é {par_impar_(par_impar)}')
        conta_vitorias =+ 1
        inicia_jogo()
        
    else:
        break

escolha_computador = par_impar_Computador(resultado)

print('-=-=-=-=-=-=-=-=-=-=-=-=-')
print('VOCE PERDEU')
print(f'Voce jogou {valor} e o computador jogou {valor_computador}. Total deu {resultado}, é {escolha_computador}')
print(f'voce ganhou {conta_vitorias} vezes da maquina')
print('-=-=-=-=-=-=-=-=-=-=-=-=-')     
       
        

    
    
    
    





    

        
    

          
