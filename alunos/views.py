from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CadastroPendenteForm, CustomUserCreationForm
from .models import AlunoAtivo

def criar_conta(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inscricao_aluno')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/criar_conta.html', {'form': form})

@login_required
def inscricao_aluno(request):
    if request.method == 'POST':
        form = CadastroPendenteForm(request.POST, request.FILES)
        if form.is_valid():
            cadastro = form.save(commit=False)
            cadastro.user = request.user
            cadastro.save()
            return redirect('inscricao_sucesso')
    else:
        form = CadastroPendenteForm()
    return render(request, 'alunos/formulario_inscricao.html', {'form': form})

def inscricao_sucesso(request):
    return render(request, 'alunos/inscricao_sucesso.html')

@login_required
def minha_conta(request):
    try:
        aluno = AlunoAtivo.objects.get(user=request.user)
        contexto = {'aluno': aluno}
    except AlunoAtivo.DoesNotExist:
        contexto = {'aluno': None}
    return render(request, 'alunos/minha_conta.html', contexto)