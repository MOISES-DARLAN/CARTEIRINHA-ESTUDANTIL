from django.contrib import admin
from .models import CadastroPendente, AlunoAtivo
from django.contrib.auth.models import User
from datetime import date, timedelta

@admin.action(description='Aprovar cadastros selecionados')
def aprovar_cadastros(modeladmin, request, queryset):
    for cadastro in queryset:
        if not User.objects.filter(email=cadastro.email).exists():
            username = cadastro.email
            password = User.objects.make_random_password()
            user = User.objects.create_user(username=username, email=cadastro.email, password=password)
            
            aluno_ativo = AlunoAtivo.objects.create(
                user=user,
                nome_completo=cadastro.nome_completo,
                matricula=cadastro.matricula,
                cpf=cadastro.cpf,
                email=cadastro.email,
                data_vencimento_assinatura=date.today() + timedelta(days=365),
                tipo_carteirinha='Digital'
            )
            
            print(f"Usuário criado para {aluno_ativo.email} com a senha: {password}")

            cadastro.delete()

class CadastroPendenteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'matricula', 'data_inscricao', 'status_validacao')
    actions = [aprovar_cadastros]

class AlunoAtivoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'matricula', 'data_vencimento_assinatura', 'status_pagamento')

admin.site.register(CadastroPendente, CadastroPendenteAdmin)
admin.site.register(AlunoAtivo, AlunoAtivoAdmin)