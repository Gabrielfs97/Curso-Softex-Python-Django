#digitar um nome e comparar com outro
#se forem iguais, imprimir "nomes são iguais", se não, imprimir "nomes diferentes"

com1 = input("digite um nome: ").lower()
com2 = input("digite um segundo nome: ").lower()

if com1 == com2:
    print("nomes são iguais !")
else:
    print("nomes diferente !")