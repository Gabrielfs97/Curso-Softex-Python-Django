from django.urls import path
from .views import (
            # ListaTarefasAPIView,
            TarefaEstatisticasView,
           # DetalheTarefaAPIView,
            DuplicarTarefaAPIView,
            ConcluirTodasTarefasView,
            MinhaView,
            TarefaListCreateAPIView,
            TarefaRetrieveUpdateDestroyAPIView,
            LogoutView,MeView,
            ChangePasswordView,
            UserStatsView,
            RegisterView,
            UserUpdateView,
            
            )



app_name = 'core'
urlpatterns = [
    
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

    path(
        'teste/',
        MinhaView.as_view(),
          name='minhaview'
          ),

    path(
        'tarefas/<int:pk>/',
          TarefaRetrieveUpdateDestroyAPIView.as_view(),
            name='tarefa-detail'
            ),
    
    path(
        'tarefas/',
          TarefaListCreateAPIView.as_view(),
            name='tarefa-list-create'
            ),

    path('tarefas/', TarefaListCreateAPIView.as_view(), name='tarefa-list-create'),

    path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroyAPIView.as_view(), name='tarefa-detail'),

    path('logout/', LogoutView.as_view(),
          name='logout'), # ← Novo endpoint

    path('me/', MeView.as_view(),
          name='me'), 

    path('change-password/', ChangePasswordView.as_view(), 
         name='change-password'),

    path('stats/', UserStatsView.as_view(),
          name='user-stats'),

    path('register/', RegisterView.as_view(), name='register'),

    path('me/update/', UserUpdateView.as_view(), name='user-update'),


]
