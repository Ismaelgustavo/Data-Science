# Crie uma lista de notas de alunos (valores float) e calcule a média aritmética.

print('Calculador de médias')

conjuntoNotas = []
cancelaLoop = True

while cancelaLoop:
    nota = int(input('Digite a nota:'))
    conjuntoNotas.append(nota)
    print('Digite 1 para adicionar mais notas.')
    print('Digite 2 para calcular a média.')
    resultadoOpcao = int(input( ))
    if resultadoOpcao == 2:
        cancelaLoop = False
        soma = sum(conjuntoNotas)
        media = soma / len(conjuntoNotas)
    

        

print(f"A média das notas é: {media: .2f}")
