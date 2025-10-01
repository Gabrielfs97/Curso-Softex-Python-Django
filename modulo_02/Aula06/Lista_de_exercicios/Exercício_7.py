"""
Exercício 7: Calculadora de Retângulos

Crie uma classe Retangulo que é inicializada com base e altura. Crie dois métodos:
1. calcular_area(): deve retornar o cálculo base * altura.
2. calcular_perimetro(): deve retornar o cálculo 2 * (base + altura).
Crie um retângulo, chame os dois métodos e imprima os resultados que eles retornam.

"""

class Retangulo:

    def __init__(self, base: int, altura:int) -> None:
        
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


retangulo = Retangulo(10, 5)


area = retangulo.calcular_area()
perimetro = retangulo.calcular_perimetro()

print(f"Área do retângulo: {area}")
print(f"Perímetro do retângulo: {perimetro}")
