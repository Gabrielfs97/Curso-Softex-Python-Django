"""
Crie duas classes: Livro e Biblioteca.
1. A classe Livro terá atributos título e autor.
2. A classe Biblioteca terá um atributo acervo, que começa como uma lista vazia [].
3. A Biblioteca deve ter dois métodos:

○ adicionar_livro(livro): recebe um objeto Livro e o adiciona à lista acervo.

○ listar_livros(): percorre a lista acervo e imprime o título e o autor de cada livro.

Crie uma biblioteca, crie alguns objetos Livro e adicione-os à biblioteca. Depois, liste os livros.

"""
class Livro:
    def __init__(self, titulo: str , autor: str) -> None:
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):

        self.acervo = []  
    
    def adicionar_livro(self, livro) -> None:

        self.acervo.append(livro)

        print(f"Livro '{livro.titulo}' adicionado ao acervo.")
    
    def listar_livros(self):

        if not self.acervo:

            print("A biblioteca está vazia.")

        else:

            print("\nLista de livros no acervo:")
            for livro in self.acervo:
                print(f"- Título: {livro.titulo}, Autor: {livro.autor}")


minha_biblioteca = Biblioteca()


livro1 = Livro("O Nome do Vento", "Patrick Rothfuss")
livro2 = Livro("1984", "George Orwell")
livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")


minha_biblioteca.adicionar_livro(livro1)
minha_biblioteca.adicionar_livro(livro2)
minha_biblioteca.adicionar_livro(livro3)


minha_biblioteca.listar_livros()