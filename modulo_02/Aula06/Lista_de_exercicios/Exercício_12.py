"""
Exercício 12: Representação Amigável (__str__)

Crie uma classe Filme com título, diretor e ano. Se você tentar dar print() em um objeto Filme,
o resultado não será muito útil. Para resolver isso, implemente o método especial __str__(self).
Este método deve retornar uma string formatada, como por exemplo: "Filme: 'De Volta para o
Futuro' (1985) - Diretor: Robert Zemeckis".

Depois de implementar, crie um objeto Filme e simplesmente use print(meu_filme).
● Dica: O que o método __str__ retorna (return) é o que será exibido quando o objeto for
impresso.

"""

class Filme:
    def __init__(self, titulo:str, diretor:str, ano:int)-> None:
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano
    
    def __str__(self):

        return f"Filme: '{self.titulo}' ({self.ano}) - Diretor: {self.diretor}"

    


meu_filme = Filme("De Volta para o Futuro", "Robert Zemeckis", 1985)


print(meu_filme)