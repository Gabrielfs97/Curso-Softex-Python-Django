from math import pi

class Circulo:
    def __init__(self, raio:int):

        self._raio = raio

    @property
    def raio(self) -> int :
        return self._raio
    
    @raio.setter
    def raio(self,novo_raio):
        if isinstance(novo_raio, int) and novo_raio > 0:
         
         self._raio = novo_raio

        else:
           print("Erro! o valor tem que ser possitivo e nao pode ser vazio")

    def calc_area(self):
      area = pi * self.raio ** 2
      return (area)
    

c1 = Circulo(10)


print(f"O raio atual é {c1.raio}")
print(f"A área atual é {c1.calc_area():.3f}")

valor_raio = int(input("digite um valor para o raio: "))
                 
c1.raio = valor_raio

print(f"O raio é {c1.raio}")
print(f"A área é {c1.calc_area():.3f}")