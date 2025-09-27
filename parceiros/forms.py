from django import forms
from .models import PropostaParceria

class PropostaParceriaForm(forms.ModelForm):
    class Meta:
        model = PropostaParceria
        fields = ['nome_fantasia', 'cnpj', 'endereco', 'categoria', 'descricao_beneficio', 'email_contato']
        widgets = {
            'nome_fantasia': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao_beneficio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'email_contato': forms.EmailInput(attrs={'class': 'form-control'}),
        }