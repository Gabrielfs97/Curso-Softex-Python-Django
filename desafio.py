"""
Comercio Padaria
Requisitos:

1- o programa tem que rodar em loop infinito até ser padado
2- o cliente pede um tipo de pão (frances, doce, forma, australiano)
3- cada pão tera uma quantidade 
4- valor do pão
5- forma de pagamento
6- forma de entrega (se for entregar)
7- dados do clente (se for entregar)
8- valor do frete por bairro
9- nome da atendente
10- codigo da entrega

"""

import random

frete = 0
valor = 0
quantidade = 0
entr = False

atendente = "Maria", 'lucia', 'vera', 'cida'

valor_f = 0.5
valor_d = 5.00
valor_for = 5.99
valor_austr = 15

quantidade_f = 15
quantidade_d = 20
quantidade_for = 15
quantidade_aust = 10

time = 0

codigo_venda = '98568', '97845', '03551', '01', '02', '21550'

random_codigo = random.choice(codigo_venda)

atendente_atual = random.choice(atendente)

while True:

    print(f"bem-vindo a padaria sonho nosso, sou a atendente {atendente_atual}")

    tipo_pao = input("qual tipo de pão você deseja? (frances, doce, forma, australiano): ").lower()

    if tipo_pao not in ["frances", "doce", "forma", "australiano"]:

        print("Tipo de pão inválido. Por favor, escolha entre frances, doce, forma ou australiano.")
        continue

    quantidade = int(input("quantidade de pães?"))

    if quantidade <= quantidade_f and tipo_pao == "frances":
        quantidade_f -= quantidade

    elif quantidade <= quantidade_d and tipo_pao == "doce":
        quantidade_d -= quantidade

    elif quantidade <= quantidade_for and tipo_pao == "forma":
        quantidade_for -= quantidade

    elif quantidade <= quantidade_aust and tipo_pao == "australiano":
        quantidade_aust -= quantidade

    else:
        
        print("Desculpe, não temos essa quantidade disponível.")

        print("caso queira pedir novamente digite 'continuar'")
        continuar = input().lower()
        if continuar == "continuar":
            continue
        else:
            break

    entrega = input("deseja entrega? (sim/não)").lower()

    if entrega == "sim":
        entr = True

        dados_cliente = input("digite seu nome: ") 

        bairro = input("qual o bairro? 1. (centro) 2. (zona sul) 3.(zona norte) ").lower()

        if bairro == "1":
            frete = 5.00
            time = 20

        elif bairro == "2":
            frete = 10.00
            time = 30

        elif bairro == "3":
            frete = 15.00
            frete = 60

        else:
            frete = 2
    
    if entrega == "nao" or entrega == "não" or entrega == "n":
        frete = 0.00

    if tipo_pao == "frances":
        valor = valor_f * quantidade 

    elif tipo_pao == "doce":
        valor = valor_d * quantidade 

    elif tipo_pao == "forma":
        valor = valor_for * quantidade 

    else:
        tipo_pao == "australiano"

        valor = valor_austr * quantidade 

    print(f"o valor total do pedido é: {valor + frete}")

    pag = input("qual a forma de pagamento? (dinheiro, pix, cartão)").lower()

    if pag == "dinheiro":

        print("Pagamento em dinheiro selecionado.")
    elif pag == "pix":

        print("Pagamento via Pix selecionado.")
    elif pag == "cartão":

        print("Pagamento com cartão selecionado.")
    else:
        print("Forma de pagamento inválida.")

    print(f"Pedido realizado com sucesso! Código da venda: {random_codigo}")

    if entr is True:

        print(f"senhor {dados_cliente} entrega confirmada")

        print(f"seu pedido chegara em {time} minutos")


    sair = input("digite sair para fechar: ")
    
    if sair.lower() == "sair":
        break