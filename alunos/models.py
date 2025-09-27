from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class CadastroPendente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=255)
    matricula = models.CharField(max_length=50, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    comprovante_matricula = models.FileField(upload_to='comprovantes/', blank=True, null=True)
    data_inscricao = models.DateTimeField(auto_now_add=True)
    
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Rejeitado', 'Rejeitado'),
    ]
    status_validacao = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')

    def __str__(self):
        return f"{self.nome_completo} - {self.user.email}"

class AlunoAtivo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=255)
    matricula = models.CharField(max_length=50, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    data_vencimento_assinatura = models.DateField()
    
    TIPO_CARTEIRINHA_CHOICES = [
        ('Digital', 'Digital'),
        ('Física', 'Física'),
    ]
    tipo_carteirinha = models.CharField(max_length=10, choices=TIPO_CARTEIRINHA_CHOICES)

    STATUS_PAGAMENTO_CHOICES = [
        ('Pago', 'Pago'),
        ('Pendente', 'Pendente'),
        ('Vencido', 'Vencido'),
    ]
    status_pagamento = models.CharField(max_length=10, choices=STATUS_PAGAMENTO_CHOICES, default='Pendente')

    def __str__(self):
        return f"{self.nome_completo} - {self.email}"

class Pagamento(models.Model):
    aluno = models.ForeignKey(AlunoAtivo, on_delete=models.CASCADE)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=6, decimal_places=2, default=50.00)
    descricao = models.CharField(max_length=255, default='Renovação Anual')

    def __str__(self):
        return f"Pagamento de {self.aluno.nome_completo} em {self.data_pagamento.strftime('%d/%m/%Y')}"