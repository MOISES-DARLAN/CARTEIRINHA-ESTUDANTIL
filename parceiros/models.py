from django.db import models

class Parceiro(models.Model):
    nome_fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    descricao_beneficio = models.TextField()
    regras_de_uso = models.TextField()

    STATUS_CHOICES = [
        ('Ativa', 'Ativa'),
        ('Inativa', 'Inativa'),
    ]
    status_parceria = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Ativa')

    def __str__(self):
        return self.nome_fantasia