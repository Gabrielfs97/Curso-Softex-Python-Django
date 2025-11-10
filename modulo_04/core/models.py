from django.db import models

# Create your models here.
class Tarefa(models.Model):

    titulo = models.CharField(max_length=200)

    # Um campo booleano (verdadeiro/falso), que por padrão é Falso
    concluida = models.BooleanField(default=False)
    # Um campo de data e hora.
    # auto_now_add=True: Salva a data e hora EXATAMENTE quando o objeto é criado
    criada_em = models.DateTimeField(auto_now_add=True)
    # Este é um "método mágico" do Python.
    # Ele diz ao Django como "chamar" um objeto Tarefa.
    # Em vez de "Tarefa object (1)", ele mostrará o título da tarefa.
    # Isso é EXTREMAMENTE útil no painel de administração.
    def __str__(self):
        return self.titulo

class Teste(models.Model):

    nome = models.CharField(max_length=200)

    local = models.CharField(max_length=20)

    hora = models.DateTimeField(auto_now_add=True)

    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
