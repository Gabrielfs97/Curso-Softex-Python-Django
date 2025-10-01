class Pessoa:
    def __init__(self,nome:str, idade:int) -> None:
        self.__nome = nome
        self.__idade = idade

    def apresentar(self):
        print(f"Ola, eu sou {self.__nome} e tenho {self.__idade} anos")
        

class Estudante(Pessoa):
    def __init__(self,nome:str,idade:int,classe:str) -> None:
        super().__init__(nome,idade)
        self.__classe = classe

    def apresentar(self):
        print(f"Ola, eu sou {self._Pessoa__nome} e tenho {self._Pessoa__idade} anos e curso {self.__classe}")


p1 = Pessoa("Marcos",20)
p2 = Estudante("Leo",30,"medio")


lista1:list[Pessoa] = [p1,p2]

for i in lista1:
    i.apresentar()