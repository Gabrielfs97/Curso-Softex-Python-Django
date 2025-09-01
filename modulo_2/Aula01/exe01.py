#list_a = [10, 99, 90, 9, 97, 9, 97, 95, 20, 30, 9, 40, 50,987789]





list_a = input("digite uma lista de numeros separados por virgula: ").split(',')


item_encontrado = 0

for i in list_a:
    string_i = str(i)
    for i in string_i:
        if i == '9':
         item_encontrado += 1
         print(''.join(string_i))

print(f"o item 9 foi encontrado {item_encontrado} vezes na lista_a") 