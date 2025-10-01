"""
2. Criando uma Cafeteira (Fácil)
Classes: GraoDeCafe, Agua e Cafeteira.
Classe GraoDeCafe:
Método:_init__(sem atributos).
Método: moer() que imprime "Os grãos de café foram moídos.".
Classe Agua:
Método:_init__(sem atributos).
Método
: aquecer() que imprime "A água está aquecida.".
Classe Cafeteira:
Atributos (Composição): grao e agua, que devem ser instâncias das classes
GraoDeCafe e Agua.
Método:_init_ que inicializa os atributos grao e agua.
Método: preparar_cafe() que chama os métodos moer() do seu grao e aquecer() da sua agua.

"""

class GraoDeCafe:
    def __init__(self):
        pass        

    def moer(self):
        print("Os grãos de café foram moídos.")

class Agua:
    def __init__(self):
        pass
    def aquecer(self):
        print("A água está aquecida.")

class Cafeteira:

    def __init__(self):
        self.grao = GraoDeCafe()
        self.agua = Agua()

    def prep_cafeee(self):
        self.grao.moer()
        self.agua.aquecer()
        


cefee = Cafeteira()

cefee.prep_cafeee()