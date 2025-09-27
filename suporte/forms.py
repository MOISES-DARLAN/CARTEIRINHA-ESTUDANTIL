from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['aluno_email', 'assunto', 'descricao_problema']
        widgets = {
            'aluno_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu e-mail de cadastro'}),
            'assunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Problema com pagamento'}),
            'descricao_problema': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Descreva seu problema em detalhes'}),
        }