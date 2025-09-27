from django.db import models
from alunos.models import AlunoAtivo

class Ticket(models.Model):
    aluno_email = models.EmailField()
    assunto = models.CharField(max_length=255)
    descricao_problema = models.TextField()
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_fechamento = models.DateTimeField(null=True, blank=True)
    
    STATUS_CHOICES = [
        ('Aberto', 'Aberto'),
        ('Em Andamento', 'Em Andamento'),
        ('Fechado', 'Fechado'),
    ]
    status_ticket = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Aberto')
    resposta_equipe = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.assunto} - {self.aluno_email}"