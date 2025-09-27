from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_ticket, name='registrar_ticket'),
    path('sucesso/', views.ticket_sucesso, name='ticket_sucesso'),
]