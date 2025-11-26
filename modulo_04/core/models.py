from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# 2. ADICIONE A NOVA RELAÇÃO
# Cada Tarefa agora DEVE estar ligada a um Projeto.
# 'related_name' é uma boa prática para consultas inversas.
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tarefas')
    titulo = models.CharField(max_length=200)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.titulo