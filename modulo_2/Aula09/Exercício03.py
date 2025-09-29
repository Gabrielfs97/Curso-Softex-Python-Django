"""

Classes: Ponto e SegmentoDeReta.
Classe Ponto:
Atributos: x e y.
Método:_init__(x, y).
Classe SegmentoDeReta:
Atributos (Composição): ponto1 e ponto2, que devem ser instâncias de Ponto.
Método:_init_(ponto1, ponto2).
Método: calcular_comprimento() que retorna a distância entre os dois pontos.
Dica: Use o módulo math e a fórmula da distância euclidiana:
(x2-x1)2+(y2-y1)2

"""

class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class SegmentoDeReta:
    def __init__(self):
        pass