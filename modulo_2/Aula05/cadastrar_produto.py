def cadastrar_produto(estoque:dict) -> None:

    """Permite o atendende cadastrar novo produto"""

    nome_produto = input("Digite o nome do novo produto (identificador)").lower().strip()

    if nome_produto in estoque:

        print("ERRO ! Esse produto já cadastrado com este identificador") 
        return
    
    try:

        nome_completo = input("Digite o nome completo do produto: ").strip()
        valor = float(input("Digite o valor do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))

        if nome_produto and nome_completo and valor > 0 and quantidade > 0 :

            estoque[nome_produto] = {"nome":nome_completo,"valor":valor,"quantidade":quantidade}
            print(f"Produto {nome_completo} cadastro com sucesso! ")

        else:
        
            print("Erro!  Dados invalidos.")

    except ValueError:
        print("Entrada de daos inválida.")        