from django.shortcuts import render
from .models import Parceiro

def lista_beneficios(request):
    parceiros_ativos = Parceiro.objects.filter(status_parceria='Ativa')
    contexto = {
        'parceiros': parceiros_ativos
    }
    return render(request, 'parceiros/lista_beneficios.html', contexto)