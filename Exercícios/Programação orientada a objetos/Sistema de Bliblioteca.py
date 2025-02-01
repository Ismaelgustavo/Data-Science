class Livro:
     
    def __init__(self, titulo, autor, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.disponibilidade = disponibilidade

    
    def exibir_livros(livro):
        if livro.disponibilidade == True:
            print(f'Titulo: {livro.titulo}')
            print(f'Autor: {livro.autor}')
            print('======================')





class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_livros = []


    def emprestar_livro(self,livro):
        if livro.disponibilidade == True:
            self.lista_de_livros.append(livro)
            livro.disponibilidade = False
            print('Livro alugado')
        else:
            print('Livro indisponível')


    def devolver_livro(self,livro):
        if livro in self.lista_de_livros:
            livro.disponibilidade = True
            self.lista_de_livros.remove(livro)
            print('Livro devolvido')
        else:
            print('Esse livro não existe na biblioteca.')



livro1 = Livro('As crônicas de gelo e fogo', 'George RR Martin', True)
livro2 = Livro('A roda do mundo', 'Ismael G Araújo', True )
livro3 = Livro('O novo mundo', 'Vera L Gonçalves Araújo', True)

usuario = Usuario('Ismael')



usuario.emprestar_livro(livro2)

Livro.exibir_livros(livro1)
Livro.exibir_livros(livro2)
Livro.exibir_livros(livro3)

usuario.devolver_livro(livro2)

Livro.exibir_livros(livro1)
Livro.exibir_livros(livro2)
Livro.exibir_livros(livro3)

        





                