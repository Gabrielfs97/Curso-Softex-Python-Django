#import random


pos = 0
#next_pos = random.randint(1,10)
print("bem vindo ao menu de ação")

while True: 
   acao = input("escolha uma ação: \n\n 1.avançar\n\n 2.recuar\n\n 3.status\n\n 4.sair\n\n")

   if acao == "1":
     pos += 1
     print("avançou para a posição:", pos)
     continue

   elif acao == "2":
       pos -= 1
       print("recuou para a posição:", pos)
       continue
   
   elif acao == "3":
       print("status atual: posição", pos)
       continue
   
   elif acao == "4":
       print("saindo...")
       break
   else:
      print("ação inválida...")
    