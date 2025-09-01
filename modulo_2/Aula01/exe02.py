
lista_a = ["azul", "verde", "amarelo", "vermelho", "branco", "preto"]

lista_b = ["roxo", "azul", "verde", "laranja", "preto", "vermelho"]

lista_c = []

itens = 0

for i in lista_a:
    for b in lista_b:
        if i == b:
            lista_c.append(i)
            itens += 1

print(lista_a)
print(lista_b)
print(f"foram encontrados {itens} itens iguais nas duas listas")
print(', '.join(lista_c))