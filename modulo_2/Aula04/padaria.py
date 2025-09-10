def dados() -> dict:
  
    """carregar e retornar os dados de produtos, frete e funcionarios"""

    return {
        "atendente":"Maria",
        "paes": {
            "frances":{"nome":"Pão Francês","valor":0.50,"quantidade":15},
            "doce":{"nome":"Pão Doce","valor":5.00,"quantidade":20},
            "forma":{"nome":"Pão de Forma","valor":5.99,"quantidade":18},
        },
        "bairros":{
            "barroco":{"nome":"Barroco","frete":5.00},
            "sao jose":{"nome":"Sao josé","frete":15.00},
        },
        "codigo_venda_base":95875,
    }


def obter_dados_cliente() -> dict:

    """solicitar e retornar os dados do cliente"""

    nome =  input("informe seu nome: ")
    return {"nome":nome}

def solicitar_forma_pagamento() -> str:

    """solitar e retornar a forma de pagamento escolhida"""

    while True:

        pagamento = input("escolha a forma de pagamento (1- Dinheiro , 2-Cartão) ")

        if pagamento == "1":
            return "Dinheiro"
        
        elif pagamento == "2":
            return "Cartão"
        
        else:
            print("forma de pagamento inválida")

def gerar_codigo_venda(codigo_base:int) -> int:

    """gera e retorna o código de venda"""

    return codigo_base + 1

def calcula_frete(bairros_disponiveis: dict) -> tuple[str,float] | None:

    """calcula o valor do frete com base no bairro de entrega"""

    print("bairros para entrega")

    for bairro in bairros_disponiveis.values():

        print(f"- {bairro["nome"]}")

    bairro_entrega_nome = input("Qual o bairro de entrega?").lower()

    bairro_encontrado = None

    for chave,bairro in bairro_encontrado.values():

        if bairro["nome"].lower() == bairro_entrega_nome:
            bairro_encontrado = chave
            break

    if not bairro_encontrado:

        print("Bairro fora da area de entrega")

    else:

        frete = bairros_disponiveis[bairro_encontrado]["frete"]

        return bairro_entrega_nome, frete
    
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