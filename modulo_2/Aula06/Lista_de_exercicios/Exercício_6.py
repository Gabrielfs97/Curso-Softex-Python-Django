"""
Exercício 6: Lógica no Saque

Na mesma classe ContaBancaria, adicione um método para sacar(valor). Este método deve
verificar se há saldo suficiente na conta.
● Se houver, ele deve subtrair o valor do saldo e imprimir "Saque realizado com sucesso.".
● Se não houver, ele deve imprimir "Saldo insuficiente." e não alterar o saldo.
Teste os dois cenários: um saque bem-sucedido e uma tentativa de sacar mais do que
tem.

"""


class ContaBancaria:

    def __init__(self, titular:str, saldo_inicial:float) -> None:
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, valor:float) -> None:

        if valor > 0:

            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        
        else:

            print("Valor de depósito deve ser positivo.")
    
    def ver_saldo(self):

        print(f"Saldo atual da conta de {self.titular}: R$ {self.saldo:.2f}")
    
    def sacar(self, valor:float) -> None:

        if valor > 0:

            if valor <= self.saldo:

                self.saldo -= valor
                print("Saque realizado com sucesso.")

                
            
            else:

                print("Saldo insuficiente.")

               
        else:

            print("Valor de saque deve ser positivo.")



conta = ContaBancaria("João", 100.00)


while True:
    try:
        print("\nBem-vindo ao sistema bancário")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver saldo")
        print("4 - Sair")

        escolha = input("O que deseja fazer? ").strip()

        if escolha == '1':
            valor_deposito = float(input("Digite o valor para depositar: "))
            conta.depositar(valor_deposito)
            continue

        elif escolha == '2':
            valor_saque = float(input("Digite o valor para sacar: "))
            conta.sacar(valor_saque)
            continue

        elif escolha == '3':
            conta.ver_saldo()
            continue

        elif escolha == '4':
            print("Saindo do sistema. Até logo!")
            break
        
        else:
            
            print("Opção inválida. Tente novamente.")
            continue

    except ValueError:
        print("Por favor, digite um número válido.")