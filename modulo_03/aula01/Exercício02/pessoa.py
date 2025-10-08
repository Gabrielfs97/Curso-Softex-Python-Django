"""
Etapa 1: A Pessoa (no arquivo pessoa.py)

Toda escola tem pessoas. Um estudante é uma pessoa,
 um professor é uma pessoa. Vamos criar um "molde" básico para qualquer pessoa.
Seu trabalho aqui:

Crie uma classe (o nosso molde) chamada Pessoa.

Essa classe deve ter um nome e uma idade.

Para garantir que as informações sejam acessadas e modificadas de forma organizada, 

implemente um método "getter" para o nome.

Um "getter" é uma forma de obter a informação de um objeto.

"""


class Pessoa:
    def __init__(self, nome:str ,idade:int, tipo:str) -> None:
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    
    def get_nome(self):
        return self.nome
    

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Tipo: {self.tipo}"