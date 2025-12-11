from django.urls import path
from .views import (
            ListaTarefasAPIView,
            TarefaEstatisticasView,
            DetalheTarefaAPIView,
            DuplicarTarefaAPIView,
            ConcluirTodasTarefasView
            )



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

    path(
        'tarefas/<int:pk>/duplicar/',
        DuplicarTarefaAPIView.as_view(),
        name='duplicar-tarefa'
        ),

    path(
        'tarefas/concluir-todas/',
        ConcluirTodasTarefasView.as_view(),
        name='concluir-todas-tarefas'
        ),
]
