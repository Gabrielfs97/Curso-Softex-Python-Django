#numero = input("digite um numero de telefone: ") 

def checador()-> str:
    numero = input("digite um numero de telefone: ")

    if not (len(numero) == 11 and numero.isdigit()):
     print("seu telefone tem que possuir 11 digitos")
    if numero.isdigit() == False:
        print("seu telefone deve conter apenas números")

    else:
     contador = {}
    for digit in numero:
        contador[digit] = contador.get(digit, 0) + 1

    num_igual = any(count >= 4 for count in contador.values())

    if num_igual:
        print("O número possui pelo menos 4 dígitos iguais. Telefone inválido!")
    else:
        formato_nacional = f"({numero[:2]}){numero[2:7]}-{numero[7:]}"
        print(f"seu telefone é válido: {formato_nacional}")
        return formato_nacional

checador()