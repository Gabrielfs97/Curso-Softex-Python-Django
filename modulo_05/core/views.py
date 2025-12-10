from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer
from django.shortcuts import get_object_or_404

class ListaTarefasAPIView(APIView):
    """Lista todas as tarefas e cria novas tarefas.

    GET /api/tarefas/ -> lista
    POST /api/tarefas/ -> cria
    """

    def get(self, request, format=None):
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TarefaEstatisticasView(APIView):
    """
    Endpoint para retornar estatísticas das tarefas.
    URL: /api/tarefas/estatisticas/
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
        """Retorna os detalhes de uma única tarefa por ID."""
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

