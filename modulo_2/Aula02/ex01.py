vendas_filtradas = []

produtos = set()

vendas = [
    ("Teclado",50,2),
    ("Mouse",25.50,4),
    ("Monitor",300,1),
    ("Fone",45,1),
    ("Webcam",75.20,2)
          ]

for nome, valor, quantidade in vendas:

    valor_total = valor * quantidade

    if valor_total >= 100:

        vendas_filtradas.append((nome,valor,quantidade))

    produtos.add(nome)

print(vendas_filtradas)

print(produtos)

