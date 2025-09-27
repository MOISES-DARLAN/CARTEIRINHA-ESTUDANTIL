from django.contrib import admin, messages
from .models import CadastroPendente, AlunoAtivo, Pagamento
from django.contrib.auth.models import User
from datetime import date, timedelta

@admin.action(description='Aprovar cadastros selecionados')
def aprovar_cadastros(modeladmin, request, queryset):
    for cadastro in queryset:
        if not User.objects.filter(email=cadastro.user.email).exists():
            # Esta lógica pode ser removida se a criação do user já é garantida
            user = cadastro.user
        else:
            user = User.objects.get(email=cadastro.user.email)

        aluno_ativo = AlunoAtivo.objects.create(
            user=user,
            nome_completo=cadastro.nome_completo,
            matricula=cadastro.matricula,
            cpf=cadastro.cpf,
            email=user.email,
            data_vencimento_assinatura=date.today() + timedelta(days=365),
            tipo_carteirinha='Digital'
        )
        cadastro.delete()

@admin.action(description='Registrar pagamento de renovação')
def registrar_renovacao(modeladmin, request, queryset):
    for aluno in queryset:
        aluno.status_pagamento = 'Pago'
        aluno.data_vencimento_assinatura = date.today() + timedelta(days=365)
        aluno.save()

        Pagamento.objects.create(
            aluno=aluno,
            descricao='Renovação Anual Manual'
        )
    modeladmin.message_user(request, "As assinaturas selecionadas foram renovadas com sucesso.", messages.SUCCESS)

class CadastroPendenteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'get_user_email', 'data_inscricao', 'status_validacao')
    actions = [aprovar_cadastros]

    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.short_description = 'Email do Usuário'

class AlunoAtivoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'matricula', 'data_vencimento_assinatura', 'status_pagamento')
    actions = [registrar_renovacao]

admin.site.register(CadastroPendente, CadastroPendenteAdmin)
admin.site.register(AlunoAtivo, AlunoAtivoAdmin)
admin.site.register(Pagamento)