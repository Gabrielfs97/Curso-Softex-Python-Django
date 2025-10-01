
"""
Exercício 9: Atributo da Classe (Funcionários da Empresa)

Crie uma classe Funcionario. Cada funcionário terá nome e salário (atributos de instância).
Agora, crie um atributo de classe chamado percentual_bonus, com o valor 1.10
(representando 10% de bônus).

Crie um método aplicar_bonus que multiplica o salário do funcionário pelo percentual_bonus
da classe. Crie dois funcionários com salários diferentes, aplique o bônus e veja o resultado.
● Dica: Um atributo de classe é definido diretamente dentro da classe, fora de qualquer
método.

"""

class Funcionario:
    
    
    def __init__(self, nome:str, salario:int) -> None:
        self.nome = nome
        self.salario = salario
    
    def aplicar_bonus(self):

        
        self.salario *= Funcionario.bonus
        print(f"Bônus aplicado para {self.nome}. Novo salário: R$ {self.salario:.2f}")

    bonus = 1.10 


funcionario1 = Funcionario("Maria", 3000.00)
funcionario2 = Funcionario("Pedro", 5000.00)


print("Antes do bônus:")
print(f"{funcionario1.nome}: R$ {funcionario1.salario:.2f}")
funcionario1.aplicar_bonus()


print("\nAntes do bônus:")
print(f"{funcionario2.nome}: R$ {funcionario2.salario:.2f}")
funcionario2.aplicar_bonus()


print("\nApós aplicação do bônus:")
print(f"{funcionario1.nome}: R$ {funcionario1.salario:.2f}")
print(f"{funcionario2.nome}: R$ {funcionario2.salario:.2f}")