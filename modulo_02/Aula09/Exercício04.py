"""

4. Dispositivos de um Computador (Fácil/Médio)

Classes: Teclado, Mouse, Monitor e Computador.
Classes Teclado, Mouse, Monitor:
Método:
init (sem atributos).
Método: ligar() que imprime uma mensagem indicando que o dispositivo está ligado (ex: "O teclado foi ativado.").

Classe Computador:
Atributos (Composição): teclado, mouse e monitor, que devem ser instâncias das classes correspondentes.
Método:_init

_ que inicializa os três atributos.

Método: ligar_computador() que chama o método ligar() de cada um dos seus dispositivos.

"""


class Teclado:
    def __init__(self):
        pass

    def ligar_t(self):
        print("Teclado ligado...")


class Mouse:
    def __init__(self):
        pass    

    def mouse_l(self):
        print("Mouse ligado...")


class Monitor:
    def __init__(self):
        pass
    def monitor_l(self):
        print("Monitor ligado...")

class Computador:
    def __init__(self):
        self.tela = Monitor()
        self.rato = Mouse()
        self.tecl = Teclado()
    
    def ligar_pc(self):

        print("Ligando pc...")

        self.tela.monitor_l()
        self.rato.mouse_l()
        self.tecl.ligar_t()

        print("Pc está ligado")

comp = Computador()

comp.ligar_pc()