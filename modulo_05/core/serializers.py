from rest_framework import serializers
from rest_framework.views import APIView
from .models import Tarefa
from datetime import date
from django.utils import timezone
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User,Group

class TarefaSerializer(serializers.ModelSerializer):
    """
    Serializer para Tarefa com segurança.
    O campo 'user' é exibido (read-only) mas NÃO aceito na entrada.
    """
    # 1. Mostra o username do usuário em vez do ID (read-only na saída)
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Tarefa
        fields = ['id', 'user', 'titulo', 'concluida', 'criada_em', 'prioridade', 'prazo', 'concluida_em']
        read_only_fields = ['id', 'user', 'criada_em', 'concluida_em']
        
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

    def __init__(self, *args, **kwargs):
        """
        Inicializa o serializer com contexto de validação
        """

        super().__init__(*args, **kwargs)
        
        self.request = self.context.get('request', None) if self.context else None
        
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

        if self.instance:  
            prioridade_atual = self.instance.prioridade
            concluida_atual = self.instance.concluida
            concluida_nova = data.get('concluida', concluida_atual)
            
           
            if not concluida_atual and concluida_nova:
                
                if prioridade_atual == 'alta': 

                    request = self.context.get('request') 
                    if request and request.method == 'PATCH':
                        raise serializers.ValidationError({
                            'non_field_errors': [
                                "Tarefas com prioridade ALTA só podem ser concluídas via PUT (atualização completa), não via PATCH."
                            ]
                        })
        
        return data
    
    def validate_prioridade(self, value):
        """
        validação especifica para o campo 'prioridade'.
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

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
     token = super().get_token(user)
    # Adicionar campos customizados ao payload
     token['username'] = user.username
     token['email'] = user.email
     token['is_staff'] = user.is_staff
     return token
    
class UserRegistrationSerializer(serializers.ModelSerializer):
# Definimos 'write_only=True' para que a senha seja aceita no cadastro (POST),
# mas NUNCA seja devolvida na resposta (Response JSON).
    password = serializers.CharField(
    write_only=True,
    required=True,
    style={'input_type': 'password'}
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def create(self, validated_data):
        """
        Intercepta a criação para usar o 'create_user' e hashear a senha.
        """

        # Extrai a senha dos dados validados
        password = validated_data.pop('password')
        user = User.object.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=password
            )
        try:
            # Busca o grupo 'Comum'
            grupo_comum = Group.objects.get(name='Comum')
            # Adiciona o usuário ao grupo
            user.groups.add(grupo_comum)
        except Group.DoesNotExist:
            # Fallback: Se o grupo não existir, o usuário é criado sem grupo.
            # Em produção, deveríamos logar um erro aqui.
            pass
            return user
