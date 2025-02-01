num1 = int(input('Digite o primeiro número: '))
sinal = str(input('Digite o sinal: '))
num2 =int(input('Digite o segundo número: '))

def calculo(num1,sinal,num2):
    if sinal == '+':
        resultado = num1 + num2
        
    elif sinal == '-':
        resultado = num1 - num2
        
    elif sinal == '*':
        resultado = num1 * num2
        
    elif sinal == '/':
        resultado = num1 / num2
    
    print(f'O resutlado é {resultado}')
    


calculo(num1,sinal,num2)
        
