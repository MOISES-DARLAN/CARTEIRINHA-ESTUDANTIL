from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CadastroPendenteForm, CustomUserCreationForm
from .models import AlunoAtivo, CadastroPendente, Pagamento

def criar_conta(request):
    if request.user.is_authenticated:
        return redirect('minha_conta')
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
    if AlunoAtivo.objects.filter(user=request.user).exists() or CadastroPendente.objects.filter(user=request.user).exists():
        return redirect('minha_conta')
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
        aluno_ativo = AlunoAtivo.objects.get(user=request.user)
        contexto = {'aluno': aluno_ativo, 'status': 'ativo'}
    except AlunoAtivo.DoesNotExist:
        try:
            cadastro_pendente = CadastroPendente.objects.get(user=request.user)
            contexto = {'cadastro': cadastro_pendente, 'status': 'pendente'}
        except CadastroPendente.DoesNotExist:
            contexto = {'status': 'nao_inscrito'}
    return render(request, 'alunos/minha_conta.html', contexto)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def minha_assinatura(request):
    aluno = AlunoAtivo.objects.get(user=request.user)
    historico_pagamentos = Pagamento.objects.filter(aluno=aluno).order_by('-data_pagamento')
    contexto = {
        'aluno': aluno,
        'historico': historico_pagamentos,
    }
    return render(request, 'alunos/minha_assinatura.html', contexto)

@login_required
def renovar_assinatura(request):
    return render(request, 'alunos/renovar_assinatura.html')