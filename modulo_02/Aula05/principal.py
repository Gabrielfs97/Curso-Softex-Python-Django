from banco_dados import dados
from dados_clientes import obter_dados_cliente
from dados_pagamento import solicitar_forma_pagamento
from gerar_codigo import gerar_codigo_venda
from calcular_frete import calcula_frete
from cadastrar_produto import cadastrar_produto
from atualizar_produto import atualizar_produto
from gerenciar_localidade import cadastrar_localidade
from processamento_principal import processar_pedido

def iniciar_programa() -> None:
    """"função que inicia o loop principal do programa de vendas"""

    banco_dados = dados()
    atendende = banco_dados["atendente"]
    paes_estoque = banco_dados["paes"]
    bairros_disponiveis = banco_dados["bairros"]
    codigo_venda = banco_dados["codigo_venda_base"]

    while True:
        print(f"--- Bem vindo(a) a Padaria Desepero, sp a atendente {atendende}.")
        print("-- Menu Principal --")
        print("1. Iniciar vendas")
        print("2. Gerenciar Produtos")
        print("3. Cadastrar Nova Localidade")
        print("4. Sair do Sistema")

        opcao_escolhida = input("Escolha uma opção: ").lower().strip()

        if opcao_escolhida == "1":
            pedido = processar_pedido(paes_estoque)

            if not pedido: 
                continue

            pao_escolhido, qtd_pedido,valor_compra, paes_estoque = pedido
            print(f"Seu pedido foi de {qtd_pedido} {pao_escolhido['nome']} ficou em R${valor_compra:.2f}.")

            forma_retirada = input("É para 1. Retirar ou 2. Entregar")
            valor_frete= 0.0


            if forma_retirada == "2":

                bairro, valor_frete  = calcula_frete(bairros_disponiveis)
                print(f"Valor do frete para o bairro {bairros_disponiveis[bairro]['nome']} é de R$ {valor_frete:.2f}")

            elif forma_retirada != "1":
                print("Opção invalida!")
                continue    

            dados_cliente = obter_dados_cliente()
            forma_pagamento = solicitar_forma_pagamento()

            valo_total_compra = valor_frete + valor_compra

            cod_venda = gerar_codigo_venda(codigo_venda)
            banco_dados["codigo_venda_base"] = cod_venda

            print("--- Resumo da venda ---")

            print(f"Cliente: {dados_cliente['nome']}.")
            print(f"Valor dos pães: R$ {valor_compra:.2f}")
            print(f"Valor do frete R$ {valor_frete:.2f}")
            print(f"Forma de pagamento: {forma_pagamento}")
            print(f"Valor total da compra R$ {valo_total_compra}")
            print(f"Código da entrega: {cod_venda}")



        elif opcao_escolhida == "2":
             pass
        elif opcao_escolhida == "3":
             pass
        elif opcao_escolhida == "4":
             print("Saindo do sistema. Até a próxima.")
             break

iniciar_programa()