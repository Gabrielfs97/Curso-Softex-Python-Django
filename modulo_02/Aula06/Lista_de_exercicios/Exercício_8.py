"""
Exercício 8: Um Carro que Anda

Crie uma classe Carro com os atributos modelo e nivel_combustivel (começando com 0).
1. Crie um método para abastecer(litros) que aumenta o nível de combustível.
2. Crie um método dirigir(distância) que consome combustível (ex: 1 litro a cada 10 km). O
método deve verificar se há combustível suficiente para a viagem. Se houver, diminua o
combustível e avise que o carro andou. Se não, avise que não há combustível.

"""



class Carro:
    def __init__(self, modelo:str, nivel_combustivel=0)-> None:
        self.modelo = modelo
        self.nivel_combustivel = nivel_combustivel
    
    def abastecer(self, litros: float) -> None:
        if litros > 0:
            self.nivel_combustivel += litros
            print(f"Abastecido {litros} litros. Nível atual: {self.nivel_combustivel} litros.")

        else:
            print("Quantidade de litros deve ser positiva.")
            
    
    def dirigir(self, distancia: float) -> None:

        consumo_por_km = 0.1  # 1 litro a cada 10 km

        combustivel_necessario = distancia * consumo_por_km
        
        if self.nivel_combustivel >= combustivel_necessario:
            
            self.nivel_combustivel -= combustivel_necessario

            print(f"O carro {self.modelo} dirigiu {distancia} km com sucesso. Combustível restante: {self.nivel_combustivel:.1f} litros.")
        
        
        else:

            print(f"Combustível insuficiente para dirigir {distancia} km.")
            print(f"Necessário: {combustivel_necessario:.1f} litros. Disponível: {self.nivel_combustivel} litros.")
    
    def ver_tanque(self):

        print(f"Nível atual de combustível no {self.modelo}: {self.nivel_combustivel} litros.")


meu_carro = Carro("Fusca")


while True:
    try:
        print("\n=== Sistema do Carro ===")
        print("1 - Abastecer")
        print("2 - Dirigir")
        print("3 - Ver tanque")
        print("4 - Sair")

        escolha = input("O que deseja fazer? ").strip()

        if escolha == '1':
            valor_abastecer = float(input("Digite a quantidade de litros para abastecer: "))
            meu_carro.abastecer(valor_abastecer)
            continue

        elif escolha == '2':
            distancia = float(input("Digite a distância em km que deseja dirigir: "))
            meu_carro.dirigir(distancia)
            continue

        elif escolha == '3':
            meu_carro.ver_tanque()
            continue

        elif escolha == '4':
            print("Saindo do sistema. Dirija com cuidado!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
            continue

    except ValueError:
        print("Por favor, digite um número válido para litros ou km.")