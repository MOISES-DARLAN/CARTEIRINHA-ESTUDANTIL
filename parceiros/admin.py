from django.contrib import admin
from .models import Parceiro

class ParceiroAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'categoria', 'status_parceria')
    list_filter = ('categoria', 'status_parceria')
    search_fields = ('nome_fantasia', 'cnpj')

admin.site.register(Parceiro, ParceiroAdmin)