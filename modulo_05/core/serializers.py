from rest_framework import serializers
from .models import Tarefa
from datetime import date
from django.utils import timezone

class TarefaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'concluida', 'criada_em', 'prioridade','prazo','concluida_em']
        read_only_fields = ['id', 'criada_em', 'concluida_em']
        
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
            },
            'concluida': {
                'required': False  
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
        Validação especifica para o campo 'prioridade'.
        """
        prioridades_validas = ['baixa', 'media', 'alta']

        if value not in prioridades_validas:

            raise serializers.ValidationError(

                f"Prioridade inválida. Escolha entre: {', '.join(prioridades_validas)}."
            )
        
        return value
        
    def validate_prazo(self, value):
        """
        validação para o campo prazo.
        """
        hoje = date.today()
        if value and value < hoje:
            raise serializers.ValidationError(
                "O prazo não pode ser uma data passada."
                )
        return value
    
    def create(self, validated_data):
        """
        Sobrescreve o metodo create para gerenciar o campo concluida_em.
        """
        
        if validated_data.get('concluida', False):
            validated_data['concluida_em'] = timezone.localtime(timezone.now())
        
        #teste
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        """
        sobrescreve o metodo update para atualizar o campo concluida_em.
        """
       
        concluida_atual = instance.concluida
        concluida_nova = validated_data.get('concluida', concluida_atual)
        
        
        if not concluida_atual and concluida_nova:
            validated_data['concluida_em'] = timezone.localtime(timezone.now())
        
       
        elif concluida_atual and not concluida_nova:
            validated_data['concluida_em'] = None
        
       #teste
        return super().update(instance, validated_data)