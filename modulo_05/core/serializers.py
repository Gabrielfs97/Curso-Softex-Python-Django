from rest_framework import serializers
from .models import Tarefa
class TarefaSerializer(serializers.ModelSerializer):
 class Meta:
    model = Tarefa
    fields = ['id', 'titulo', 'concluida', 'criada_em']
    read_only_fields = ['id', 'criada_em']

 def validate(self, data):
     """
     Validação de objeto completo (múltiplos campos).

     Exemplo: Tarefas com palavra "urgente" não podem
     começar como concluídas.
     """
     titulo = data.get('titulo', '').lower()
     concluida = data.get('concluida', False)
     if 'urgente' in titulo and concluida:
         raise serializers.ValidationError("Tarefas urgentes não podem ser criadas como concluídas.")
     return data