from django.urls import path
from . import views

urlpatterns = [
    path('suporte/', views.registrar_ticket, name='registrar_ticket'),
    path('suporte/sucesso/', views.ticket_sucesso, name='ticket_sucesso'),
]