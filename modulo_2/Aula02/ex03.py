

acessos =[
    ("Pedro","sucesso"),
    ("Ana","falha"),
    ("Maria","sucesso"),
    ("Pedro","falha"),
    ("Ana","falha")
          ]

entrada = set()

negado = set()

for nome, login in acessos:
    if login == "sucesso":
        entrada.add(nome) 

    else:
        negado.add(nome)


print("usuarios com pelo menos um login bem-sucedido")
print(entrada)

print("usuarios que tiveram somente logins com falha")
print(negado.difference(entrada))