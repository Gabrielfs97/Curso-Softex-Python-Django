
#classe cria um "molde" para cachorro
class Cachorro:
    def __init__(self, nome:str,cor:str) -> None:
        self.nome = nome
        self.cor = cor
        self.falar = "seloco n compensa"
    
    def latir(self, ) -> None:
        print(f"{self.nome} diz: {self.falar}")


meu_cachorro = Cachorro("Rex","preto")

# nome e cor são aributos (variaves) da class Cachorro
# por isso não são chamadas com parênteses: ()
print(meu_cachorro.nome)
print(meu_cachorro.cor)
meu_cachorro.latir()