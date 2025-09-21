"""
Exercício 3: Ensinando a se Apresentar

Adicione um método (uma "ação") à sua classe Pessoa chamado apresentar. Esse método
deve imprimir uma frase como: "Olá, meu nome é [nome] e eu tenho [idade] anos." Chame
esse método para os objetos "João" e "Maria".

"""


class pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        self.apresenta = "Olá, tudo bem?" + f" Eu me chamo {self.nome} e tenho {self.idade} anos."
            
    
    def apresentar(self) -> None:
        print(f"{self.nome} diz: {self.apresenta}")

    
pessoa1 = pessoa("João", 25)
pessoa2 = pessoa("Maria", 30)

pessoa1.apresentar()
pessoa2.apresentar()