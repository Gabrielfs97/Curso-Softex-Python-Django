

ham = 10
lancho = 0.2

print("Bem-vindo ao menu")

while True:

    pedido = input("Escolha seu lanche: ")

    if pedido == "hamburguer":

        print(f"o valor do hamburguer é R${ham}")
        
        cupom = input("Você possui cupom de desconto? (sim/não)").lower()

        if cupom == "sim":
            desconto = input("Digite o cupom: ")

            if desconto == "lancho20":
                print("Você ganhou 20% de desconto")
                print(f"novo valor é R$ {ham - (ham * lancho)}")

        elif cupom == "não":
            print("Sem problemas! Aproveite seu lanche.")
        else:
            print("Cupom inválido.")
        
    else:
        print("Desculpe, apenas possuímos hamburguer no momento.")
    print("seu pedido foi finalizado")    
    break