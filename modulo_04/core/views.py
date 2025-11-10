from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarefa
from .models import Teste
# Create your views here.

     

def home(request): 
    todas_as_tarefas = Tarefa.objects.all()
    teste_teste = Teste.objects.all()
# Vamos retornar a resposta HTTP mais simples: um texto HTML 
    context = {
'nome_usuario': 'Gabriel',
'tecnologias': ['Python', 'Django','CSS', 'Models', 'Admin',],
'tarefas': todas_as_tarefas,
'teste': teste_teste
}
    return render(request, 'home.html', context)



def mainPage(request):
    return HttpResponse("<h2>Catapimbas, segundo olá, mundo!")