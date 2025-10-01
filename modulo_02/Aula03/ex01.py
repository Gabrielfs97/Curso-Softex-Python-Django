contatos = {}


while True:

    print("\n----contatos----")
    print("1-adicionar contato")
    print("2-buscar contato")
    print("3-sair\n")

    opt = input("digite uma opção: ")

    if opt == '1':

        try:
            nome = input("digite o nome: ")
            numero = input("digite o numero do contato: ")
            cidade = input("digite a cidade do contato: ")
            numero = int(numero)

            contatos = {nome: numero,"Cidade": cidade }
            print(f"{nome} foi adicionado")

            print(contatos)

        except KeyError:
            print("digite apenas letras no nome e cidade")
        except ValueError:
            print("digite apenas numeros...")

    elif opt == '2':

        nome = input("digite o nome da pessoa que gostaria de buscar: ")
        contato = contatos.get(nome,"contato nao encontrato")
        numero = contatos.get(numero,"numero nao encontrato")
        print(contato)
        
    elif opt == '3':
        break