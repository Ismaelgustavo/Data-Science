# Crie uma função chamada gerar_senha() que recebe um número inteiro representando o tamanho da senha e retorna uma string com caracteres aleatórios.

import random
import string

def gerar_senha(tamanho):
  """Gera uma senha aleatória com o tamanho especificado.

  Args:
    tamanho: Um número inteiro representando o tamanho da senha.

  Returns:
    Uma string com a senha gerada.
  """

  # Define os caracteres que podem compor a senha
  caracteres = string.ascii_letters + string.digits + string.punctuation

  # Gera uma senha aleatória
  senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

  return senha

# Exemplo de uso:
tamanho_senha = 12
senha_gerada = gerar_senha(tamanho_senha)
print(senha_gerada)