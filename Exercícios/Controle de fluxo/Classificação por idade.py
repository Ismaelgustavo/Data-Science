idade = int(input('Digite sua idade: '))

if 0 <= idade < 13:
    print('Criança')
elif  13 <= idade < 18:
    print('Adolescente')
elif 18 <= idade < 60:
    print('Adulto')
else:
    print('Idoso')            

