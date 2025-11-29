
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome  
        self.__email = email  
    
    @property
    def email(self):
        return self.__email

    
    @email.setter
    def email(self, novo_email):
        if "@" in novo_email:
            self.__email = novo_email
            print(f"Sucesso: E-mail alterado para {novo_email}")
        else:
            print(f"Erro: O e-mail '{novo_email}' é inválido (falta @).") 