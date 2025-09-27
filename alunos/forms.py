from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CadastroPendente

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escolha um nome de usuário'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu melhor e-mail'}),
        }

class CadastroPendenteForm(forms.ModelForm):
    class Meta:
        model = CadastroPendente
        fields = ['nome_completo', 'matricula', 'cpf', 'comprovante_matricula']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sua matrícula universitária'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'comprovante_matricula': forms.FileInput(attrs={'class': 'form-control'}),
        }