def contador_de_vogais(palavra: str) -> int:
    """Conta o número de vogais e consoantes em uma string fornecida. """

    palavra = palavra.lower().strip()

    contador_vogais = 0
    contador_consoantes = 0

    vogais = "aeiou"

    for char in palavra:
        if char.isalpha():
            if char in vogais:
                contador_vogais += 1
            else:
                contador_consoantes += 1
        return{

        print(f"A palavra possui {len(palavra)} caracteres no total."),
        print(f"A palavra possui {contador_vogais} vogais e {contador_consoantes} consoantes.")
      
        
        }


def verificador_de_palindromo(palavra: str) -> bool:
    """Verifica se uma string é um palíndromo. retorna True se for políndromo ou False se não for. """

    palavra = palavra.lower().strip()
    palavra = ''.join(char for char in palavra if char.isalnum())  
    palavra_invertido = palavra[::-1]

    if palavra == palavra_invertido:
        print("É um palíndromo.")
        return True
    else:
        print("Não é um palíndromo.")
        return False



palavra_entrada = input("Digite uma palavra: ")

print("---------Resultados---------")
print()

contador_de_vogais(palavra_entrada)
verificador_de_palindromo(palavra_entrada)

