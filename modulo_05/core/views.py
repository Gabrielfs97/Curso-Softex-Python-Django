from urllib import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Tarefa
from .serializers import (
    TarefaSerializer,
    CustomTokenObtainPairSerializer,
    UserRegistrationSerializer,
    )
from django.shortcuts import get_object_or_404
from datetime import timedelta
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .permissions import IsGerente


class ListaTarefasAPIView(APIView):
    """
    Lista todas as tarefas e cria novas tarefas.
    """
    def get(self, request, format=None):
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TarefaSerializer(
            data=request.data,
            context={'request': request}  # contexto
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TarefaEstatisticasView(APIView):
    """
    endpoint para retornar estatísticas das tarefas.
    uRL: /api/tarefas/estatisticas/
    """
    
    def get(self, request, format=None):
        
        total = Tarefa.objects.count()
        
        
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = Tarefa.objects.filter(concluida=False).count()
        
        
        if total != (concluidas + pendentes):
            
            total = Tarefa.objects.count()
            concluidas = Tarefa.objects.filter(concluida=True).count()
            pendentes = total - concluidas
        
        
        taxa_conclusao = concluidas / total if total > 0 else 0
        
       
        resposta = {
            "total": total,
            "concluidas": concluidas,
            "pendentes": pendentes,
            "taxa_conclusao": round(taxa_conclusao, 2)
        }
        
        return Response(resposta, status=status.HTTP_200_OK)

class DetalheTarefaAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Tarefa, pk=pk)

    def get(self, request, pk, format=None):
        """retorna os detalhes de uma única tarefa por ID."""
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """
         permite atualização completa da tarefa.
        """
        tarefa = self.get_object(pk)
        
        serializer = TarefaSerializer(
            tarefa, 
            data=request.data,
            context={'request': request}  # contexto
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        """
        atualizaçao parcial - proibido conclusão de tarefas de alta prioridade.
        """
        tarefa = self.get_object(pk)
        

        serializer = TarefaSerializer(
            tarefa, 
            data=request.data, 
            partial=True,
            context={'request': request}  # contexto
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DuplicarTarefaAPIView(APIView):

    """
    endpoint para duplicar uma tarefa existente.
    POST /api/tarefas/<pk>/duplicar/
    """
    
    def post(self, request, pk, format=None):

        try:

            tarefa_original = get_object_or_404(Tarefa, pk=pk)
            data = request.data
            
            
            novo_titulo = data.get('novo_titulo')
            if not novo_titulo:
                novo_titulo = f"{tarefa_original.titulo} (Cópia)"
            
            
            manter_concluida = data.get('manter_concluida', False)
            concluida_copia = tarefa_original.concluida if manter_concluida else False
            
            # calcula o novo prazo aqui o
            adicionar_dias = data.get('adicionar_dias_prazo', 0)
            try:
                adicionar_dias = int(adicionar_dias)
            except (ValueError, TypeError):
                adicionar_dias = 0
            
            novo_prazo = None
            if tarefa_original.prazo:
                novo_prazo = tarefa_original.prazo + timedelta(days=adicionar_dias)
            
            # aqui prepara os dados para a nova tarefa
            dados_tarefa_copia = {
                'titulo': novo_titulo,
                'concluida': concluida_copia,
                'prioridade': tarefa_original.prioridade,
                'prazo': novo_prazo,

                #teste
                #'user': tarefa_original.user if hasattr(tarefa_original, 'user') else None
            }
            
           # cria uma nova tarefa usando o serializer
            serializer = TarefaSerializer(
                data=dados_tarefa_copia,
                context={'request': request}  #contexto
            )
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as e:
            return Response(
                {'error': f'Erro ao duplicar tarefa: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ConcluirTodasTarefasView(APIView):
    """
    endpoint para concluir todas as tarefas pendentes em lote.
    PATCH /api/tarefas/concluir-todas/
    """
    
    def patch(self, request, format=None):
        """
        marca todas as tarefas pendentes como concluidas.
        RESPEITANDO: Tarefas de prioridade alta NÃO podem ser concluidas em lote
        """
        try:
            # busca todas as tarefas pendentes
            
            tarefas_pendentes = Tarefa.objects.filter(concluida=False)
            
            if not tarefas_pendentes.exists():
                return Response(
                    {
                        'message': 'Não há tarefas pendentes para concluir.',
                        'tarefas_afetadas': 0
                    },
                    status=status.HTTP_200_OK
                )
            
            # contador
            tarefas_concluidas = 0
            tarefas_com_erro = 0
            tarefas_alta_ignoradas = 0  
            erros_detalhados = []
            
            # para cada tarefa pendente, usa o serializer para marcar como concluída
            for tarefa in tarefas_pendentes:
                try:

                    # tarefas de prioridade alta não podem ser concluídas em lote
                    if tarefa.prioridade == 'alta':
                        tarefas_alta_ignoradas += 1
                        erros_detalhados.append({
                            'tarefa_id': tarefa.id,
                            'titulo': tarefa.titulo,
                            'erro': 'Tarefa com prioridade ALTA não pode ser concluída em lote (use PUT individual).'
                        })
                        continue  
                    
                    # tenta marcar como concluída
                    serializer = TarefaSerializer(
                        tarefa, 
                        data={'concluida': True}, 
                        partial=True,
                        context={'request': request}  # contexto
                    )
                    
                    if serializer.is_valid():
                        serializer.save()
                        tarefas_concluidas += 1
                    else:
                        tarefas_com_erro += 1
                        erros_detalhados.append({
                            'tarefa_id': tarefa.id,
                            'titulo': tarefa.titulo,
                            'erro': serializer.errors
                        })
                        
                except Exception as e:
                    tarefas_com_erro += 1
                    erros_detalhados.append({
                        'tarefa_id': tarefa.id,
                        'titulo': tarefa.titulo,
                        'erro': str(e)
                    })
            
            # resposta com um resumo
            resposta = {
                'message': f'Concluídas {tarefas_concluidas} tarefa(s) pendente(s).',
                'tarefas_afetadas': tarefas_concluidas,
                'tarefas_com_erro': tarefas_com_erro,
                'tarefas_alta_ignoradas': tarefas_alta_ignoradas,
                'total_tarefas_pendentes': tarefas_pendentes.count(),
                'nota': 'Tarefas com prioridade ALTA foram ignoradas (só podem ser concluídas via PUT individual).'
            }
            
            # sinaliza erro se houver
            if erros_detalhados:
                resposta['erros_detalhados'] = erros_detalhados[:5]  # Limita a 5
            
            return Response(resposta, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Erro ao processar requisição em lote: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
class MinhaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {'message': f'Olá, {request.user.username}! Você está autenticado.'},
            status=status.HTTP_200_OK
        )
        

class TarefaListCreateAPIView(generics.ListCreateAPIView):
    """
    Lista tarefas e permite a criação de novas tarefas.
    PROTEGIDA: Requer autenticação JWT.
    """
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated] # ← Proteção

    def get_queryset(self):
        """
        Sobrescreve o comportamento padrão para retornar APENAS
        os dados pertencentes ao usuário logado.
        """
    # 1. Recupera o usuário validado pelo JWT
        user = self.request.user
    # 2. Retorna o filtro. O Django fará o WHERE user_id = X no banco.
        return Tarefa.objects.filter(user=user)

    # MÉTODO CHAVE: Injeta o usuário logado antes de salvar o objeto
    def perform_create(self, serializer):
        """
        Associa a tarefa ao usuário logado (request.user) automaticamente.
        """
     # request.user é garantido como autenticado pelo IsAuthenticated
        serializer.save(user=self.request.user)

class TarefaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalhes de tarefa, atualização e exclusão.
    PROTEGIDA: Requer autenticação JWT.
    """
    
    serializer_class = TarefaSerializer

    # MÉTODO CHAVE: Garante que apenas o dono da tarefa possa acessá-la

    def get_queryset(self):
        """
        Filtra as tarefas para retornar apenas as do usuário logado.
        """
        user = self.request.user
        return Tarefa.objects.filter(user=user)
    def get_permissions(self):
        """
        Instancia e retorna a lista de permissões que esta view requer,
        dependendo do método HTTP da requisição.
        """
        if self.request.method == 'DELETE':
# Para deletar: Precisa estar logado E ser Gerente
# A ordem importa: primeiro checa login, depois o grupo
            return [IsAuthenticated(), IsGerente()]
# Para GET, PUT, PATCH: Basta estar logado (e ser dono, garantido pelo queryset)
        return [IsAuthenticated()]


class CustomTokenObtainPairView(TokenObtainPairView):
    """View que usa o serializer customizado."""
    serializer_class = CustomTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()  # Adiciona o token à lista negra
            return Response(
                {"detail": "Logout realizado com sucesso."},
                status=status.HTTP_205_RESET_CONTENT
            )
        except Exception:  # Captura exceções como token_not_valid
            return Response(
                {"detail": "Token inválido."},
                status=status.HTTP_400_BAD_REQUEST
            )
class MeView(APIView):
    """
    Endpoint para retornar dados do usuário autenticado.
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        return Response(
            {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_staff': user.is_staff,
            'date_joined': user.date_joined
            },
        )
    
class ChangePasswordView(APIView):
    """
    Endpoint para alteração de senha do usuário autenticado.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
     
     user = request.user

     old_password = request.data.get('old_password')

     new_password = request.data.get('new_password')

     if not old_password or not new_password:
        return Response(
                {'error': 'Os campos "old_password" e "new_password" são obrigatórios'},
                status=status.HTTP_400_BAD_REQUEST)

     if not user.check_password(old_password):
        return Response( {'error': 'Senha atual incorreta'},status=400)
    
     if old_password == new_password:
            return Response(
                {'error': 'A nova senha deve ser diferente da senha atual'},
                status=status.HTTP_400_BAD_REQUEST
            )
     
     user.set_password(new_password)
     user.save()

     return Response({'detail': 'Senha alterada com sucesso'})   
    
class UserStatsView(APIView):

    """
    Endpoint para retornar estatísticas das tarefas do usuário autenticado.
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        
        # Filtra as tarefas apenas do usuário logado
        tarefas_usuario = Tarefa.objects.filter(user=user)
        
        # Calcula estatísticas
        total_tarefas = tarefas_usuario.count()
        concluidas = tarefas_usuario.filter(concluida=True).count()
        pendentes = total_tarefas - concluidas
        
        # Calcula taxa de conclusão e evita a divisão por zero
        taxa_conclusao = concluidas / total_tarefas if total_tarefas > 0 else 0
        
        # Resultado
        return Response({
            "total_tarefas": total_tarefas,
            "concluidas": concluidas,
            "pendentes": pendentes,
            "taxa_conclusao": round(taxa_conclusao, 2)
        }, status=status.HTTP_200_OK)
    
class RegisterView(generics.CreateAPIView):
    """
    Endpoint para cadastro de novos usuários.
    Acesso: Público (Qualquer um pode criar conta).
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny] # Sobrescreve o padrão global
    serializer_class = UserRegistrationSerializer