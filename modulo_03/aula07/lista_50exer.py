def atualizar_dicionario():
    """
    Cria um dicionário e o atualiza com entradas do usuário.

    Esta função solicita continuamente ao usuário uma chave e um valor.
    Ela tenta adicionar ou atualizar a chave no dicionário. O processo
    para quando o usuário insere uma chave vazia.

    Retorna:
        dict: O dicionário finalizado com as chaves e valores inseridos.
    """
    dados = {}  # Inicializa um dicionário vazio

    while True:  # Inicia um loop infinito
        # Usamos um bloco try/except aqui para lidar com o fim das entradas simuladas nos testes
        try:
            chave = input("Digite a chave (ou pressione Enter para sair): ")
        except EOFError:
            break

        if not chave:  # Verifica se a chave é uma string vazia
            print("Chave vazia recebida. Encerrando o loop.")
            break  # Interrompe o loop

        novo_valor = input(f"Digite o novo valor para a chave '{chave}': ")

        try:
            # Tenta adicionar/atualizar o par chave-valor no dicionário
            dados[chave] = novo_valor
            print(f"Dicionário atualizado: {dados}\n")
        except Exception as e:
            # Captura exceções genéricas que possam ocorrer (embora raras neste caso)
            print(f"Ocorreu um erro ao atualizar o dicionário: {e}\n")

    return dados

# O código de execução pode ficar aqui, mas não será executado pelo pytest
if __name__ == "__main__":
    meu_dicionario_final = atualizar_dicionario()

    print("\n--- Dicionário Final ---")
    if meu_dicionario_final:
        for chave, valor in meu_dicionario_final.items():
            print(f"Chave: '{chave}', Valor: '{valor}'")
    else:
        print("O dicionário está vazio.")