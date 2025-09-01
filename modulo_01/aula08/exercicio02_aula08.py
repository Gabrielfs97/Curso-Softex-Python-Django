palavra = input("Digite uma palavra: ").lower()

texto_cod = palavra.replace("a", "1").replace("e", "2").replace("i", "3").replace("o", "4").replace("u", "5")
print(f"Palavra modificada: {texto_cod}")

texto_decod = palavra.replace("1", "a").replace("2", "e").replace("3", "i").replace("4", "o").replace("5", "u")
print(f"A palavra original é: {texto_decod}")    



'''
vogais = "aeiou"
vogal_cod = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}

nova_palavra = ""

for letra in palavra:
    if letra in vogais:
        nova_palavra += vogal_cod[letra]
    else:
        nova_palavra += letra

print(f"Palavra modificada: {nova_palavra}")
print(f"A palavra original é: {palavra}")
'''