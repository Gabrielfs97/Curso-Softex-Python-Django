from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

     

def home(request): 
# Vamos retornar a resposta HTTP mais simples: um texto HTML 
    context = {
'nome_usuario': 'Gabriel',
'tecnologias': ['Python', 'Django', 'HTML', 'CSS']
}
    return render(request, 'home.html', context)



def mainPage(request):
    return HttpResponse("<h2>Catapimbas, segundo olá, mundo!")