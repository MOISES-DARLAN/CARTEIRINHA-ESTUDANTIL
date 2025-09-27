from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('inscricao/', views.inscricao_aluno, name='inscricao_aluno'),
    path('inscricao/sucesso/', views.inscricao_sucesso, name='inscricao_sucesso'),
    path('minha-conta/', views.minha_conta, name='minha_conta'),
    path('minha-assinatura/', views.minha_assinatura, name='minha_assinatura'),
    path('renovar-assinatura/', views.renovar_assinatura, name='renovar_assinatura'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('criar-conta/', views.criar_conta, name='criar_conta'),
    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), 
        name="reset_password"),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), 
        name="password_reset_done"),
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), 
        name="password_reset_confirm"),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), 
        name="password_reset_complete"),
]