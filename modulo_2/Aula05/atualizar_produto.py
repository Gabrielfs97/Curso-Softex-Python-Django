def atualizar_produto(estoque: dict) -> None:

    """Permite ao atendente atualizar um produto existente"""
    nome_produto = input("Digite o nome do protudo para atualizar (identificador): ").lower().strip()

    if nome_produto not in estoque:
        print("Produto não cadastrado")
        return  
    
    print(f"Produto'{estoque[nome_produto]}' selecionado.")
    escolha = input("o que deseja atualizar?\n \
          1 - valor;\n \
          2 - Quantidade")
    
    try:

        if escolha == "1":

            novo_valor = float(input("Digite o novo valor do produto: "))

            if novo_valor > 0:

                estoque[nome_produto]["valor"] = novo_valor
                print("Valor atualizado com sucesso!")
                print(f"o novo valor do {estoque[nome_produto]} é R$ {novo_valor:.2f}")
            
            else:

                print("valor inválido.")
                
        elif escolha == "2":

            nova_quantidade = int(input("Digite a nova quantidade do produto"))

            if nova_quantidade > 0 :

                estoque[nome_produto]["quantidade"] += nova_quantidade
                print(f"Quantidade atual de {estoque[nome_produto]["quantidade"]} itens.")
            
            else:
                
                print("Quantidade invalida.")
        
        else:

            print("opção invalida!")

    except ValueError:
        print("Erro! Entrada de dados invalida. Digite apenas números.")