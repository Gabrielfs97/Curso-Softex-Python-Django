notas = [
    ("Ana",9.5),
    ("Joao",8.0),
    ("Maria",10.0),
    ("Pedro",7.5),
    ("Ana",10.0),
    ("Carlos",6.5)
]

media_nota = 7
nota_max = 0
abaixo = set()
max = set()


for nome, nota in notas:
    
    if nota >= nota_max:

        nota_max =+ nota

    if nota == nota_max:

        max.add(nome)

    if nota <= media_nota:

        abaixo.add(nome)

print(nota_max)

print(max)

print(abaixo)