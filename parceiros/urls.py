from django.urls import path
from . import views

urlpatterns = [
    path('beneficios/', views.lista_beneficios, name='lista_beneficios'),
]