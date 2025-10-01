"""
Exercício 4: Molde de um Produto

Crie uma nova classe chamada Produto. Todo produto deve ter nome e preço. Depois, crie
duas instâncias:
1. Um "Caderno" que custa 15.50.
2. Uma "Caneta" que custa 3.00.
Imprima o nome e o preço de cada produto.

"""


class Produto:
    def __init__(self, nome:str , preco: float)-> None:
        self.nome = nome
        self.preco = preco

caderno = Produto("Caderno", 15.50)
caneta = Produto("Caneta", 3.00)

print(f"{caderno.nome}: R$ {caderno.preco}")
print(f"{caneta.nome}: R$ {caneta.preco}")

