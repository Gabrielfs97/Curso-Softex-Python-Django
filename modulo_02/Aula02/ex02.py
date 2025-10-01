
#produtos_disponiveis = set()

estoque_principal = [ 
    ("Camiseta",121),
    ("Tenis",122),
    ("Bone",123),
    ("Sandalia",124),
    ("Mochila",125)

]
estoque_online = [
    ("Sandalia",124),
    ("Mochila",125),
    ("Terno",255),
    ("Short",265)
]

produtos_loja = set(estoque_principal)

produtos_site = set(estoque_online)

disp = produtos_loja.intersection(produtos_site)

dif_fis = produtos_loja.difference(produtos_site)

dif_sit = produtos_site.difference(produtos_loja)

print(f"Produtos disponiveis na loja e no site: {disp}")

print(f"Produto disponivel apenas na loja fisica: {dif_fis}")

print(f"Produtos apenas no site: {dif_sit}")