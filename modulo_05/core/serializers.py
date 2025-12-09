from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'concluida', 'criada_em', 'prioridade']
        read_only_fields = ['id', 'criada_em']
        
        extra_kwargs = {
            'prioridade': {
                'validators': [],
                'error_messages': {
                    'invalid_choice': "Prioridade inválida. Escolha entre: baixa, media, alta."
                }
            }
        }

    def validate(self, data):
        """
        Validação de objeto completo (múltiplos campos).
        """
        titulo = data.get('titulo', '').lower()
        concluida = data.get('concluida', False)

        if 'urgente' in titulo and concluida:
            raise serializers.ValidationError({
                'non_field_errors': ["Tarefas urgentes não podem ser criadas como concluídas."]
            })
        
        return data
    
    def validate_prioridade(self, value):
        """
        Validação específica para o campo 'prioridade'.
        """
        prioridades_validas = ['baixa', 'media', 'alta']

        if value not in prioridades_validas:

            raise serializers.ValidationError(
                
                f"Prioridade inválida. Escolha entre: {', '.join(prioridades_validas)}."
            )
        
        return value