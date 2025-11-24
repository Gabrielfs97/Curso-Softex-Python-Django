from django.shortcuts import redirect, render, get_object_or_404 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponse
from .models import Tarefa
from .models import Teste
from .forms import TarefaForm
# Create your views here.

     
@login_required 
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
        todas_as_tarefas = Tarefa.objects.all(user=request.user).order_by('-criada_em')

# Vamos retornar a resposta HTTP mais simples: um texto HTML 
    context = {
'nome_usuario': request.user.username,
'tecnologias': ['Python', 'Django','CSS', 'Models', 'Admin',],
'tarefas': todas_as_tarefas,
'teste': teste_teste,
'form': form,
}
    return render(request, 'home.html', context)



def mainPage(request):
    return HttpResponse("<h2>Catapimbas, segundo olá, mundo!")

def register(request): 
# Se a requisição for POST, o usuário enviou o formulário 
    if request.method == 'POST': 
# Cria uma instância do formulário com os dados enviados 
        form = UserCreationForm(request.POST) 
# Verifica se o formulário é válido (ex: senhas batem, username não existe) 
    if form.is_valid(): 
        user = form.save() # Salva o novo usuário no banco 
        login(request, user) # Faz o login automático do usuário 
        return redirect('home') # Redireciona para a home 
# Se a requisição for GET, o usuário apenas visitou a página 
    else: 
        form = UserCreationForm() # Cria um formulário de cadastro vazio 
# Prepara o contexto e renderiza o template 
        context = {'form': form} 
    return render(request, 'register.html', context) 

@login_required 
def concluir_tarefa(request, pk): 
# 2. Modifique o 'get_object_or_404' 
# Busque a Tarefa pela 'pk' E ONDE o 'user' é o 'request.user' 
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user) 
if request.method == 'POST': 
    tarefa.concluida = True 
    tarefa.save()
return redirect('home')

@login_required 
def deletar_tarefa(request, pk): 
# 3. Faça o mesmo filtro de segurança aqui 
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user) 
if request.method == 'POST': 
    tarefa.delete() 
return redirect('home')