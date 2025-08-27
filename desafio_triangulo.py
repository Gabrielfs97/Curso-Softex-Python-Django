"""
Desafio de Programação: Validação de Triângulo
Seu objetivo: Escrever um algoritmo em Python que determine se três valores, fornecidos pelo usuário,
 podem formar um triângulo.

As Regras do Jogo
1- Teste se a entrada de dados é um número.
2- Se for um número teste se é positivo
3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas condições importantes:

A soma: A soma de quaisquer dois lados deve ser maior que o terceiro lado.

lA<lB+lC

lB<lA+lC

lC<lA+lB

A diferença: O valor absoluto da diferença entre dois lados deve ser menor que o terceiro lado.

lA>∣lB−lC∣

lB>∣lA−lC∣

lC>∣lA−lB∣

Dica: use o método abs() para ter o valor absoluto de um número.
"""

print("#### verificador de triângulo ! ########")

la = input("digite o valor do lado A: ")

lb = input("digite o valor do lado B: ")

lc = input("digite o valor do lado C: ")
         

if la.isdigit() and lb.isdigit() and lc.isdigit():

    la = int(la)
    lb = int(lb)
    lc = int(lc)

    if la > 0 and lb > 0 and lc > 0:

        if (la < lb + lc) \
        and (lb < la + lc) \
        and (lc < la + lb):

            if (la > abs(lb - lc)) and (lb > abs(la - lc)) and (lc > abs(la - lb)):

                print(f"os valores {la},{lb},{lc} podem formar um triângulo !")

            else:
            
                print(f"os valores {la}, {lb}, {lc} não podem formar um triângulo !")

        else:
            print(f"os valores {la}, {lb}, {lc} não podem formar um triângulo !")
    else:
        print(f"os valores {la}, {lb}, {lc} devem ser positivos !")
else:
    print("os valores devem ser numéricos !")