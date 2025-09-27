from django.urls import path
from . import views

urlpatterns = [
    path('beneficios/', views.lista_beneficios, name='lista_beneficios'),
    path('seja-parceiro/', views.registrar_proposta, name='registrar_proposta'),
    path('seja-parceiro/sucesso/', views.proposta_sucesso, name='proposta_sucesso'),
]