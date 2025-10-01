"""
Exercício 2: Criando Pessoas Reais

Usando a classe Pessoa que você criou, crie dois objetos:
1. Uma pessoa chamada "João", com 25 anos.
2. Uma pessoa chamada "Maria", com 30 anos.
Depois de criá-los, imprima o nome e a idade de cada um para confirmar que deu certo

"""

class pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    
pessoa1 = pessoa("João", 25)
pessoa2 = pessoa("Maria", 30)

print(f"Uma pessoa chamada {pessoa1.nome} tem {pessoa1.idade} anos.")

print(f"Uma pessoa chamada {pessoa2.nome} tem {pessoa2.idade} anos.")