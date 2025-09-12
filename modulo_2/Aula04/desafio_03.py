"""
Crie um sistema de cadastro e login de usuários, ele deve:

1 - Permitir que um usuário se registre com um nome e senha.
2 - Validar a senha para garantir que ela seja segura 
(com pelo menos 8 caracteres e uma mistura de letras e números).
3 - Permitir que o usuário faça login digitando seu nome e senha.
4 - Informar se o login foi bem-sucedido ou falhou.

"""

def validar_senha(senha: str) -> bool:

    """Valida se a senha é segura, retornando True se for segura ou False se não for."""
    
    if len(senha) < 8:
        return False
    
    tem_letra = False

    tem_numero = False

    for char in senha:
        if char.isalpha():
            tem_letra = True
        elif char.isdigit():
            tem_numero = True

        if tem_letra and tem_numero:
            break

    return tem_letra and tem_numero


def registrar_usuario(nome: str, senha: str) -> None:

    """Registra um novo usuário com nome e senha."""
    
    usuarios[nome] = senha
    



usuarios = {}  

while True:

    print("1. Registrar")
    print("2. Login")
    print("3. Sair")

    escolha = input("Escolha uma opção (1 ,2 ,3 ): ")

    if escolha == '1':

        nome = input("Digite um nome de usuário: ").strip()

        if nome in usuarios:

            print("Nome de usuário já existe. Tente outro.")
            continue

        senha = input("Digite uma senha: ").strip()

        if not validar_senha(senha):

            print("Senha fraca. Deve ter pelo menos 8 caracteres, incluindo letras e números.")

            continue

        registrar_usuario(nome, senha)


        print("Usuário registrado com sucesso!")

    elif escolha == '2':

        nome = input("Digite seu nome de usuário: ").strip()
        senha = input("Digite sua senha: ").strip()

        if usuarios.get(nome) == senha:
            print("Login bem-sucedido!")
        else:
            print("Falha no login. Nome ou senha incorretos.")

    elif escolha == '3':
        print("Saindo do sistema.")
        break

    else:
        print("Opção inválida. Tente novamente.")