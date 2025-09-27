# alunos/forms.py

from django import forms
from .models import CadastroPendente

class CadastroPendenteForm(forms.ModelForm):
    class Meta:
        model = CadastroPendente
        fields = ['nome_completo', 'matricula', 'cpf', 'email', 'comprovante_matricula']
        
        # Adicione este dicionário de widgets
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sua matrícula universitária'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seuemail@dominio.com'}),
            'comprovante_matricula': forms.FileInput(attrs={'class': 'form-control'}),
        }