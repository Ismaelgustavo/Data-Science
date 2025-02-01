'''
Contador de Frequências:

Escreva uma função chamada contar_frequencias() que recebe uma lista de números e retorna um dicionário onde:
As chaves são os números da lista.
Os valores são as quantidades de vezes que cada número aparece.

'''
def contar_frequencias(lista_numeros):
  """Conta a frequência de cada número em uma lista.

  Args:
    lista_numeros: Uma lista de números.

  Returns:
    Um dicionário onde as chaves são os números e os valores são suas frequências.
  """

  frequencias = {}
  for numero in lista_numeros:
    if numero in frequencias:
      frequencias[numero] += 1
    else:
      frequencias[numero] = 1
  return frequencias

# Exemplo de uso:
minha_lista = [1, 2, 2, 3, 3, 3, 4]
resultado = contar_frequencias(minha_lista)
print(resultado)


