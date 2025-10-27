import pytest
from lista_50exer import atualizar_dicionario

def test_adicionar_e_atualizar_itens(monkeypatch):
    """
    Testa a adição de novos itens e a atualização de um item existente.
    """
    # Lista de entradas simuladas:
    # 1. Chave 'nome', Valor 'Ana'
    # 2. Chave 'idade', Valor '30'
    # 3. Chave 'nome', Valor 'Beatriz' (atualização)
    # 4. Chave vazia '' para sair do loop
    entradas_simuladas = ['nome', 'Ana', 'idade', '30', 'nome', 'Beatriz', '']
    
    # Criamos um iterador para que cada chamada a 'input' pegue o próximo item da lista
    iterador_de_entradas = iter(entradas_simuladas)
    
    # Usamos monkeypatch para substituir a função 'input'
    # A lambda function simplesmente pega o próximo item do nosso iterador
    monkeypatch.setattr('builtins.input', lambda _: next(iterador_de_entradas))

    # Executa a função que queremos testar
    resultado = atualizar_dicionario()

    # Define o dicionário que esperamos como resultado final
    esperado = {
        'nome': 'Beatriz',
        'idade': '30'
    }

    # Verifica se o resultado é o esperado
    assert resultado == esperado

def test_parar_com_chave_vazia_imediatamente(monkeypatch):
    """
    Testa o caso em que o usuário digita uma chave vazia na primeira tentativa,
    resultando em um dicionário vazio.
    """
    # A única entrada é uma string vazia para sair do loop
    entradas_simuladas = ['']
    iterador_de_entradas = iter(entradas_simuladas)
    monkeypatch.setattr('builtins.input', lambda _: next(iterador_de_entradas))

    resultado = atualizar_dicionario()

    # O dicionário deve estar vazio
    assert resultado == {}

def test_com_numeros_e_caracteres_especiais(monkeypatch):
    """
    Testa se o dicionário lida corretamente com chaves e valores diversos.
    """
    entradas_simuladas = [
        'item-1', 'valor-A', 
        '123', '456', 
        'cidade', 'Maricá-RJ',
        ''
    ]
    iterador_de_entradas = iter(entradas_simuladas)
    monkeypatch.setattr('builtins.input', lambda _: next(iterador_de_entradas))

    resultado = atualizar_dicionario()
    
    esperado = {
        'item-1': 'valor-A',
        '123': '456',
        'cidade': 'Maricá-RJ'
    }

    assert resultado == esperado