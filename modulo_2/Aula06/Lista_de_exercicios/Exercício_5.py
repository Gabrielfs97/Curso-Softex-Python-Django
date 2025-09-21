"""
Exercício 5: Conta Bancária

Crie uma classe ContaBancaria. Toda conta deve começar com um titular e um saldo inicial.
Crie um método depositar(valor) que some um valor ao saldo da conta. Crie um objeto,
deposite um valor e imprima o novo saldo.

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
        





conta = ContaBancaria("João", 100.00)


while True:

    try:
        print("\nbem-vindo ao sistema bancário")
        print("1 - Depositar")
        print("2 - para ver saldo")
        print("3 - Sair")

        escolha = input("O que deseja fazer ? ").strip()

        if escolha == '1':

            valor_deposito = float(input("Digite o valor para depositar: ")).strip()
            conta.depositar(valor_deposito)
            continue

        elif escolha == '2':

            conta.ver_saldo()
            continue

        elif escolha == '3':

            print("Saindo do sistema. Até logo!")
            break
            
        else:
            
            print("Opção inválida. Tente novamente.")
            continue


    except ValueError:

        print("Por favor, digite um número válido.")
