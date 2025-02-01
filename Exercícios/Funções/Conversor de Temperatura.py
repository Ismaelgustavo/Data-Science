temperatura = int(input('Digite uma temperatura '))
print('Digite C para Celsius ou F para  Fahrenheit')
unidadeDeTemperatura = input()


def celsiusParaFahrenheit(temperatura):
    temp = (temperatura * 9/5) + 32
    return temp


def fahrenheitParaCelsius(temperatura):
    temp = (temperatura - 32) * 5/9
    return temp




if unidadeDeTemperatura == 'F' or unidadeDeTemperatura == 'f':
    f = celsiusParaFahrenheit(temperatura)
    print(f'A temperatura em Fahrenheit é {f: .1f}°')

elif unidadeDeTemperatura == 'C' or unidadeDeTemperatura == 'c':
    c = fahrenheitParaCelsius(temperatura)
    print(f'A temperatura em Celsius é {c: .1f}°')

