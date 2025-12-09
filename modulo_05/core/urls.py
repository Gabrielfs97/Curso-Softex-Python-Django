from django.urls import path
from .views import ListaTarefasAPIView, TarefaEstatisticasView


app_name = 'core'
urlpatterns = [
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/estatisticas/', TarefaEstatisticasView.as_view(), name='tarefa-estatisticas'),
]
