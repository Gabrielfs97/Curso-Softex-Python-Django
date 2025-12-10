from rest_framework import serializers
from .models import Tarefa
from datetime import date

class TarefaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'concluida', 'criada_em', 'prioridade','prazo','concluida_em']
        read_only_fields = ['id', 'criada_em']
        
        extra_kwargs = {
            'prioridade': {
                'validators': [],
                'error_messages': {
                    'invalid_choice': "Prioridade inválida. Escolha entre: baixa, media, alta."
                }

            },
            'prazo': {
                'required': False,
                'allow_null': True,
            }
        }

    def validate(self, data):
        """
        Validação de objeto completo (múltiplos campos).
        """
        titulo = data.get('titulo', '').lower()
        concluida = data.get('concluida', False)
        prazo = data.get('prazo', None)
        hoje = date.today()
        

        if 'urgente' in titulo and concluida:
            raise serializers.ValidationError({
                'non_field_errors': ["Tarefas urgentes não podem ser criadas como concluídas."]
            })
    
        if prazo and prazo < hoje:
            raise serializers.ValidationError({
                'prazo': "O prazo não pode ser uma data passada."
            })
        
        if not concluida and prazo is None:
            raise serializers.ValidationError({
                'prazo': ["Para tarefas pendentes, o prazo é obrigatório."]
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
        
    def validate_prazo(self, value):
        """
        Validação específica para o campo 'prazo'.
        """
        hoje = date.today()
        if value and value < hoje:
            raise serializers.ValidationError(
                "O prazo não pode ser uma data passada."
                )
        return value