from django import forms
from .models import Tarefa # Importe o Model
from projects.models import Project

# Esta classe herda de 'ModelForm'
class TarefaForm(forms.ModelForm):
# A "mágica" acontece aqui, na classe 'Meta'
    def __init__(self, *args, **kwargs):
# 2. Capture o 'user' que será passado pela view
        user = kwargs.pop('user', None)
    # 3. Chame o construtor original (pai)
        super(TarefaForm, self).__init__(*args, **kwargs)
# 4. A MÁGICA:
# Se o 'user' foi passado...
        if user:
    # ...filtre o 'queryset' (a lista de opções) do campo 'project'
    # para mostrar apenas os projetos onde o 'user' é o usuário logado.
            self.fields['project'].queryset = Project.objects.filter(user=user)
    class Meta:
        model = Tarefa
    # 5. Adicione 'project' aos campos do formulário
        fields = ['titulo', 'project']