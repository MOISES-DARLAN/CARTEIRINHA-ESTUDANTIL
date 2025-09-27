from django.shortcuts import render, redirect
from .forms import TicketForm

def registrar_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_sucesso')
    else:
        form = TicketForm()
    return render(request, 'suporte/formulario_ticket.html', {'form': form})

def ticket_sucesso(request):
    return render(request, 'suporte/ticket_sucesso.html')