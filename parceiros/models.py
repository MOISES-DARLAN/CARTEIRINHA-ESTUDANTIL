from django.db import models

class PropostaParceria(models.Model):
    nome_fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    descricao_beneficio = models.TextField()
    email_contato = models.EmailField()
    data_proposta = models.DateTimeField(auto_now_add=True)
    
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Aprovada', 'Aprovada'),
        ('Rejeitada', 'Rejeitada'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')

    def __str__(self):
        return self.nome_fantasia

class Parceiro(models.Model):
    nome_fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    descricao_beneficio = models.TextField()
    regras_de_uso = models.TextField(blank=True)

    STATUS_CHOICES = [
        ('Ativa', 'Ativa'),
        ('Inativa', 'Inativa'),
    ]
    status_parceria = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Ativa')

    def __str__(self):
        return self.nome_fantasia