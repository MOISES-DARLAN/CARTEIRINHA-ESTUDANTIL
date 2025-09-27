from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.minha_conta, name='home'),
    path('inscricao/', views.inscricao_aluno, name='inscricao_aluno'),
    path('inscricao/sucesso/', views.inscricao_sucesso, name='inscricao_sucesso'),
    path('minha-conta/', views.minha_conta, name='minha_conta'),
    path('minha-assinatura/', views.minha_assinatura, name='minha_assinatura'),
    path('renovar-assinatura/', views.renovar_assinatura, name='renovar_assinatura'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('criar-conta/', views.criar_conta, name='criar_conta'),
]