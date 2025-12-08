from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer

class ListaTarefasAPIView(APIView):

    def get(self, request, format=None):
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        
 # 1. INSTANCIAR: Criar serializer com dados recebidos
        serializer = TarefaSerializer(data=request.data)

    # 2. VALIDAR: Checar se os dados são válidos
        if serializer.is_valid():
    # 3. SALVAR: Persistir no banco de dados
         serializer.save()

    # 4. RESPONDER: Retornar objeto criado + status 201
         return Response(serializer.data,status=status.HTTP_201_CREATED)

    # 5. ERRO: Retornar erros de validação + status 400
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)