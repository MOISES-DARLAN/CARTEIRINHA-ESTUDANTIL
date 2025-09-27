from django.shortcuts import render, redirect
from .models import Parceiro
from .forms import PropostaParceriaForm

def lista_beneficios(request):
    parceiros_ativos = Parceiro.objects.filter(status_parceria='Ativa')
    contexto = {
        'parceiros': parceiros_ativos
    }
    return render(request, 'parceiros/lista_beneficios.html', contexto)

def registrar_proposta(request):
    if request.method == 'POST':
        form = PropostaParceriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proposta_sucesso')
    else:
        form = PropostaParceriaForm()
    return render(request, 'parceiros/formulario_proposta.html', {'form': form})

def proposta_sucesso(request):
    return render(request, 'parceiros/proposta_sucesso.html')