from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CadastroPendenteForm
from .models import AlunoAtivo

def inscricao_aluno(request):
    if request.method == 'POST':
        form = CadastroPendenteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inscricao_sucesso')
    else:
        form = CadastroPendenteForm()
    return render(request, 'alunos/formulario_inscricao.html', {'form': form})

def inscricao_sucesso(request):
    return render(request, 'alunos/inscricao_sucesso.html')

@login_required
def minha_conta(request):
    aluno = AlunoAtivo.objects.get(user=request.user)
    return render(request, 'alunos/minha_conta.html', {'aluno': aluno})