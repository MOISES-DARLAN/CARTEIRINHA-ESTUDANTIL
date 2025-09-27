from django.contrib import admin
from .models import CadastroPendente, AlunoAtivo
from django.contrib.auth.models import User
from datetime import date, timedelta

@admin.action(description='Aprovar cadastros selecionados')
def aprovar_cadastros(modeladmin, request, queryset):
    for cadastro in queryset:
        aluno_ativo = AlunoAtivo.objects.create(
            user=cadastro.user,
            nome_completo=cadastro.nome_completo,
            matricula=cadastro.matricula,
            cpf=cadastro.cpf,
            email=cadastro.user.email,
            data_vencimento_assinatura=date.today() + timedelta(days=365),
            tipo_carteirinha='Digital'
        )
        cadastro.delete()

class CadastroPendenteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'get_user_email', 'data_inscricao', 'status_validacao')
    actions = [aprovar_cadastros]

    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.short_description = 'Email do Usuário'

class AlunoAtivoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'matricula', 'data_vencimento_assinatura', 'status_pagamento')

admin.site.register(CadastroPendente, CadastroPendenteAdmin)
admin.site.register(AlunoAtivo, AlunoAtivoAdmin)