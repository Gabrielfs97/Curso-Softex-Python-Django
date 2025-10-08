from pessoa import Pessoa

class estudante(Pessoa):
    def __init__(self, nome:str, idade:int, tipo:str, matricula:int, curso:str) -> None:
        super().__init__(nome, idade, tipo)
        self._matricula = matricula
        self._curso = curso
