from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Tarefa
from .models import Teste
from .forms import TarefaForm
# Create your views here.

     

def home(request): 
    todas_as_tarefas = Tarefa.objects.all()
    teste_teste = Teste.objects.all()
    if request.method == 'POST':
        # Cria uma instância do form e preenche com os dados do POST
        form = TarefaForm(request.POST)
        # 4. O Django valida os dados (max_length, etc.)
        if form.is_valid():
        # 5. Salva o objeto no banco de dados!
         form.save()
         return redirect('home')
        # 6. Redireciona de volta para a 'home'
        # Isso é o Padrão "Post-Redirect-Get" (PRG
        
        # Se o form NÃO for válido, o código continua e
        # o 'form' (com os erros) será enviado para o template
        # 7. Lógica de GET: Se o usuário apenas visitou a página
    else:
        form = TarefaForm() # Cria um formulário vazio
        # 8. A busca de dados (fora dos 'ifs', pois é necessária sempre)
        todas_as_tarefas = Tarefa.objects.all().order_by('-criada_em')

# Vamos retornar a resposta HTTP mais simples: um texto HTML 
    context = {
'nome_usuario': 'Gabriel',
'tecnologias': ['Python', 'Django','CSS', 'Models', 'Admin',],
'tarefas': todas_as_tarefas,
'teste': teste_teste,
'form': form,
}
    return render(request, 'home.html', context)



def mainPage(request):
    return HttpResponse("<h2>Catapimbas, segundo olá, mundo!")

