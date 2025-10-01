
lista_int = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

lista_a = []

for i in lista_int:
    primo = True
    if i < 2:
        primo = False
    else:
        for n in range(2, int(i**0.5) + 1):
            if i % n == 0:
                primo = False
                break
    if primo:
        lista_a.append(i)
        
print(lista_a)