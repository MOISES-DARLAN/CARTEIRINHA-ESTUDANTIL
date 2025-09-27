from django.contrib import admin, messages
from .models import Parceiro, PropostaParceria
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

@admin.action(description='Aprovar propostas e criar parceiros')
def aprovar_propostas(modeladmin, request, queryset):
    for proposta in queryset.filter(status='Pendente'):
        Parceiro.objects.create(
            nome_fantasia=proposta.nome_fantasia,
            cnpj=proposta.cnpj,
            endereco=proposta.endereco,
            categoria=proposta.categoria,
            descricao_beneficio=proposta.descricao_beneficio,
            status_parceria='Ativa'
        )
        proposta.status = 'Aprovada'
        proposta.save()

        contexto_email = {'nome_parceiro': proposta.nome_fantasia}
        assunto = render_to_string('parceiros/email_proposta_aprovada_assunto.txt', contexto_email)
        corpo = render_to_string('parceiros/email_proposta_aprovada_corpo.txt', contexto_email)
        send_mail(assunto.strip(), corpo, settings.DEFAULT_FROM_EMAIL, [proposta.email_contato])

@admin.action(description='Rejeitar propostas selecionadas')
def rejeitar_propostas(modeladmin, request, queryset):
    for proposta in queryset.filter(status='Pendente'):
        proposta.status = 'Rejeitada'
        proposta.save()

        contexto_email = {'nome_parceiro': proposta.nome_fantasia}
        assunto = render_to_string('parceiros/email_proposta_rejeitada_assunto.txt', contexto_email)
        corpo = render_to_string('parceiros/email_proposta_rejeitada_corpo.txt', contexto_email)
        send_mail(assunto.strip(), corpo, settings.DEFAULT_FROM_EMAIL, [proposta.email_contato])

class PropostaParceriaAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'cnpj', 'categoria', 'data_proposta', 'status')
    list_filter = ('status', 'categoria')
    actions = [aprovar_propostas, rejeitar_propostas]

class ParceiroAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'categoria', 'status_parceria')
    list_filter = ('categoria', 'status_parceria')
    search_fields = ('nome_fantasia', 'cnpj')

admin.site.register(PropostaParceria, PropostaParceriaAdmin)
admin.site.register(Parceiro, ParceiroAdmin)