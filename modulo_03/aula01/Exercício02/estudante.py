from pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome:str, idade:int, tipo:str, matricula:int, curso:str) -> None:
        super().__init__(nome, idade, tipo)
        self.matricula = matricula
        #self._materia =
        self.curso = curso
        self.notas = {}



    def adicionar_nota(self, materia:str, nota:float):

        if materia not in self.notas:

            self.notas[materia] = []

        self.notas[materia].append(nota)
        
    def __str__(self):
      
        info_pessoa = super().__str__()  
        info_notas = f"Notas: {self.notas}"
        return f"{info_pessoa}, Matrícula: {self.matricula}\n{info_notas}"