from django.contrib import admin
from .models import Parceiro, PropostaParceria

@admin.action(description='Aprovar propostas selecionadas e criar parceiros')
def aprovar_propostas(modeladmin, request, queryset):
    for proposta in queryset:
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

class PropostaParceriaAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'cnpj', 'categoria', 'data_proposta', 'status')
    list_filter = ('status', 'categoria')
    actions = [aprovar_propostas]

class ParceiroAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'categoria', 'status_parceria')
    list_filter = ('categoria', 'status_parceria')
    search_fields = ('nome_fantasia', 'cnpj')

admin.site.register(PropostaParceria, PropostaParceriaAdmin)
admin.site.register(Parceiro, ParceiroAdmin)