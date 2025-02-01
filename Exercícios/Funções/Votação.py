from datetime import datetime

ano_nascimento = int(input('Em que ano vc nasceu? '))


def voto(nascimento):
    
    data_atual = datetime.now().year
    idade = data_atual - nascimento
    return idade


idade = voto(ano_nascimento) 

if idade < 18:
    print(f'Sua idade é {idade} anos, seu voto está NEGADO')

elif 18 <= idade <= 60:
    print(f'Sua idade é {idade} anos, seu voto é OBRIATÓRIO')

else:
    print(f'Sua idade é {idade} anos, seu voto é OPCIONAL')


