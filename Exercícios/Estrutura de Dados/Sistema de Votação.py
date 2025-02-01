'''
Crie um programa que registra votos em um dicionário:
As chaves são os nomes dos candidatos.
Os valores são o número de votos que cada candidato recebeu.
Permita que o usuário vote em candidatos e mostre o total de votos no final.
'''

candidatos = {

    'Ismael': 0,
    'Gustavo':0,
    'Vera':0,
    'branco': 0

}
voto_eleitor = 0


def mostra_resultado():
    print('RESULTADO:')
    print('=-=--=-=-=-=-')
    for candidato,votos in candidatos.items():
        print(f'Canditado {candidato}: {votos} votos')
        print('_______________________________________')
        break


def registra_votos(valor_voto):
    opcao = 0

    if valor_voto == 45:
        candidatos['Ismael'] += 1
    elif valor_voto == 10:
        candidatos['Gustavo']  += 1   
    elif valor_voto == 50:
        candidatos['Vera'] += 1 
    elif valor_voto == 0:
        candidatos['branco'] += 1 
    elif valor_voto == 1:
        mostra_resultado()
  
    
    print('Deseja confirmar o voto?')
    print('1-Sim/2-Não')
    opcao = int(input(' '))
    if opcao == 1:
        return
    else:
        registra_votos(voto_eleitor)   

while True:

    print('CANDIDATOS:')
    print('Ismael - 45')
    print('Gustavo - 10')
    print('Vera - 50')
    print('Voto em branco - 0')
    print('Encerrar votação - 1 ')
    print('=-=-=-=-=-=-=-=')
    voto_eleitor = int(input(('Digite o valor do seu candidato ')))
    registra_votos(voto_eleitor)
    


