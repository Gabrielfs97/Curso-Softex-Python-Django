"""

2. Nivel Médio: Sistema de Mídia

Crie uma classe base Midia com um construtor que recebe titulo e duracao_seg. Adicione um
método exibir() que imprime o título e a duração.

Crie duas classes filhas, Musica e Video, que herdam de Midia:
· Musica deve ter um atributo adicional artista e sobrescrever o método exibir() para
incluir o nome do artista.

· Video deve ter um atributo adicional resolucao e sobrescrever o método exibir() para
incluir a resolução.

No script principal, crie um dicionário para organizar sua coleção de mídias, usando as
chaves 'musicas' e 'videos'. 

Crie objetos de Musica e Video e os adicione a suas respectivas
listas dentro do dicionário. 

Por fim, itere sobre as listas e chame o método exibir() para cada
item, demonstrando o polimorfismo de forma organizada.

"""





class Midia:
    def __init__(self, titulo: str, duracao_seg: int):
        self.titulo = titulo
        self.duracao_seg = duracao_seg

    def exibir(self):
        print(f"Título: {self.titulo}, Duração: {self.duracao_seg} segundos")

class Musica(Midia):
    def __init__(self, titulo: str, duracao_seg: int, artista: str):
        super().__init__(titulo, duracao_seg)
        self.artista = artista

    def exibir(self):
        print(f"Título: {self.titulo}, Duração: {self.duracao_seg} segundos, Artista: {self.artista}")

class Video(Midia):
    def __init__(self, titulo: str, duracao_seg: int, resolucao: str):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao

    def exibir(self):
        print(f"Título: {self.titulo}, Duração: {self.duracao_seg} segundos, Resolução: {self.resolucao}")

dicionario1 = {"musicas": [], "videos": []}

m1 = Musica("Imagine",183,"John Lennon")
v1 = Video("Inception",8880,"1080p")

dicionario1["musicas"].append(m1)
dicionario1["videos"].append(v1)


for musica in dicionario1["musicas"]:
    musica.exibir()


for video in dicionario1["videos"]:
    video.exibir()