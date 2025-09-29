"""
Lista de Exercícios de Composição

1. Montando um Carro (Fácil)

Classes: Motor e Carro.
Classe Motor:
Método:_init_(sem atributos).
Método: ligar() que imprime "O motor ligou.".

Classe Carro:

Atributo (Composição): motor, que deve ser uma instância de Motor.
Método:_init_ que inicializa o atributo motor.
Método: ligar_carro() que chama o método ligar() do seu objeto motor.

"""

class Motor:

    def __init__(self):
        pass
    def motor_ligado(self):
        print("carro ligado...")

    def motor_desligado(self):
        print("carro desligado...")


class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar_carro(self):
        self.motor.motor_ligado()
        print("Ligando carro...")

car = Carro()

car.ligar_carro()