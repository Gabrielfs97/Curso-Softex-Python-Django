from django.db import models
from django.contrib.auth.models import User
class Tarefa(models.Model):
    
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]
    # MODIFICAÇÃO TEMPORÁRIA: null=True, blank=True
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,  # Permite NULL no banco
        blank=True,  # Permite vazio em formulários
        related_name='tarefas',
        verbose_name='Usuário'
    )

    titulo = models.CharField(max_length=200, verbose_name='Título')
    concluida = models.BooleanField(default=False, verbose_name='Concluída')
    criada_em = models.DateTimeField(auto_now_add=True, verbose_name='Criada em')
    
    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES,
        default='media',
        verbose_name='Prioridade'
    )

    prazo = models.DateField(
        null=True,
        blank=True,
        verbose_name='Prazo'
    )

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['-criada_em']

    def __str__(self):
        status = 'Concluída' if self.concluida else 'Pendente'
        prazo_str = f" - Prazo: {self.prazo}" if self.prazo else ""
        return f"{self.titulo} ({status}) - Prioridade: {self.get_prioridade_display()}{prazo_str}"