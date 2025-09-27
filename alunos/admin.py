from django.contrib import admin, messages
from .models import CadastroPendente, AlunoAtivo, Pagamento
from django.contrib.auth.models import User
from datetime import date, timedelta
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.crypto import get_random_string

@admin.action(description='Aprovar cadastros selecionados')
def aprovar_cadastros(modeladmin, request, queryset):
    for cadastro in queryset:
        user = cadastro.user
        
        # Forma correta de gerar uma senha aleatória
        password = get_random_string(length=12)
        user.set_password(password)
        user.save()

        aluno_ativo = AlunoAtivo.objects.create(
            user=user,
            nome_completo=cadastro.nome_completo,
            matricula=cadastro.matricula,
            cpf=cadastro.cpf,
            email=user.email,
            data_vencimento_assinatura=date.today() + timedelta(days=365),
            tipo_carteirinha='Digital'
        )
        
        contexto_email = {
            'nome_aluno': aluno_ativo.nome_completo,
            'email_aluno': aluno_ativo.email,
            'senha_temporaria': password,
        }
        
        assunto = render_to_string('alunos/email_aprovado_assunto.txt', contexto_email)
        corpo = render_to_string('alunos/email_aprovado_corpo.txt', contexto_email)
        
        try:
            send_mail(assunto.strip(), corpo, settings.DEFAULT_FROM_EMAIL, [aluno_ativo.email], fail_silently=False)
        except Exception as e:
            modeladmin.message_user(request, f"Erro ao enviar e-mail para {aluno_ativo.email}: {e}", messages.ERROR)

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