"""
Crie um programa que funcione como uma calculadora de bolso.
 Ele deve ser capaz de fazer adição, subtração, multiplicação e divisão.

O programa deve sempre mostrar um menu de opções, pedir ao usuário para escolher a operação e digitar dois números.
 No final, ele exibe o resultado da conta. Se houver algum erro,

 como uma divisão por zero ou o usuário digitar algo que não é um número,
   o programa deve avisar e não travar.

"""

def adicionar(x, y)-> float:

    """soma dois numeros e retorna o resultado"""

    return x + y

def subtrair(x, y) -> float:

    """subtrai dois numeros e retorna o resultado"""

    return x - y

def multiplicar(x, y) -> float:

    """multiplica dois numeros e retorna o resultado"""

    return x * y   
 
def dividir(x, y) -> float:

    """divide dois numeros e retorna o resultado""" 
    if y == 0:
     
     return "Erro: Divisão por zero não é permitida."
    
    return x / y

def menu_da_calculadora() -> None:

    """Exibe o menu da calculadora."""

    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def escolha_da_operacao() -> str:
   """pega a escolha do usuario e retorna a escolha"""
   while True:
    escolha = input("Digite sua escolha (1, 2, 3, 4, 5): ")

    if escolha in ('1', '2', '3', '4', '5'):
        return escolha
    else:
        print("Escolha inválida. Por favor, selecione uma operação válida.")

def calculadora() -> None:
     """Função principal da calculadora."""
     while True:

      menu_da_calculadora()

      escolha_da_operacao()
      
      try:

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

      except ValueError:

        print("Entrada inválida. Por favor, digite números válidos.")
        continue

      if escolha_da_operacao == '1':

        print(f"{num1} + {num2} = {adicionar(num1, num2)}")

      elif escolha_da_operacao == '2':

        print(f"{num1} - {num2} = {subtrair(num1, num2)}")

      elif escolha_da_operacao == '3':

        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

      elif escolha_da_operacao == '4':

        resultado = dividir(num1, num2)

        print(f"{num1} / {num2} = {resultado}")
            
      if escolha_da_operacao == '5':
        print("Encerrando a calculadora. Até mais!")
        break

print("Bem-vindo à Calculadora de Bolso!")
calculadora()