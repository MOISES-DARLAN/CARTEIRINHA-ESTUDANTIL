from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('assunto', 'aluno_email', 'status_ticket', 'data_abertura')
    list_filter = ('status_ticket', 'data_abertura')
    search_fields = ('assunto', 'aluno_email', 'descricao_problema')
    readonly_fields = ('data_abertura', 'data_fechamento')

    fieldsets = (
        ('Detalhes do Ticket', {
            'fields': ('aluno_email', 'assunto', 'descricao_problema', 'status_ticket')
        }),
        ('Datas', {
            'fields': ('data_abertura', 'data_fechamento')
        }),
        ('Resposta', {
            'fields': ('resposta_equipe',)
        }),
    )

admin.site.register(Ticket, TicketAdmin)