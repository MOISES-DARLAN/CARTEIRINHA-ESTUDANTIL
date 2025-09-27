from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('inscricao/', views.inscricao_aluno, name='inscricao_aluno'),
    path('inscricao/sucesso/', views.inscricao_sucesso, name='inscricao_sucesso'),
    path('minha-conta/', views.minha_conta, name='minha_conta'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]