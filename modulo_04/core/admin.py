from django.contrib import admin
from .models import Tarefa
from .models import Teste

class TarefaAdmin(admin.ModelAdmin): 
    list_display = ('titulo', 'user', 'concluida', 'criada_em')
    

admin.site.register(Tarefa,TarefaAdmin)
admin.site.register(Teste)