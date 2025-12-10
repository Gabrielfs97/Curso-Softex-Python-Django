from django.urls import path
from .views import ListaTarefasAPIView, TarefaEstatisticasView, DetalheTarefaAPIView


app_name = 'core'
urlpatterns = [
    path(
        'tarefas/',
        ListaTarefasAPIView.as_view(),
        name='lista-tarefas'
        ),

    path(
        'tarefas/<int:pk>/',
         DetalheTarefaAPIView.as_view(),
         name='detalhe-tarefa'
         ),

    path(
        'tarefas/estatisticas/',
        TarefaEstatisticasView.as_view(), 
        name='tarefa-estatisticas'
        ),
]
