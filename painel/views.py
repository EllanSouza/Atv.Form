from django.shortcuts import render
from painel.forms import EstudanteForm

def cadastro_aluno(request):
    if request.method == 'POST':
        form = EstudanteForm(request.POST) 
        if form.is_valid():
            form.save()
            form = EstudanteForm()
    else:
        form = EstudanteForm()

    return render(request,'cadastro.html', { 'form' : form})