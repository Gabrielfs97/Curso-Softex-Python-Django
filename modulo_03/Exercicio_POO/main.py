from usuario import Usuario
from canais import Email, SMS
from sistema import SistemaAlerta

def main():

    print("---- 1. TESTE DE SEGURANÇA ----")

    cliente = Usuario("Lucas", "Lucas@email.com")

    print(f"E-mail inicial do cliente: {cliente.email}")

    cliente.email = "Lucas.com" 
    cliente.email = "Lucas_novo@email.com" 

    print(f"E-mail atual do cliente: {cliente.email}")

    print("\n---- 2. TESTE DE EMAIL ----")

    canal_email = Email()
    sistema = SistemaAlerta(cliente, canal_email)
    sistema.disparar("O servidor caiu!")

    print("\n---- 3. TESTE DE SMS ----")

    canal_sms = SMS()

    sistema_sms = SistemaAlerta(cliente, canal_sms)
    sistema_sms.disparar("Pagamento aprovado!")

if __name__ == "__main__":
    main()