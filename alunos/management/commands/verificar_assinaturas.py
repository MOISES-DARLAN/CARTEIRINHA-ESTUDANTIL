from django.core.management.base import BaseCommand
from alunos.models import AlunoAtivo
from django.utils import timezone

class Command(BaseCommand):
    help = 'Verifica as assinaturas de todos os alunos ativos e atualiza o status para "Vencido" se a data de vencimento já passou.'

    def handle(self, *args, **options):
        hoje = timezone.now().date()
        alunos_vencidos = AlunoAtivo.objects.filter(
            data_vencimento_assinatura__lt=hoje,
            status_pagamento='Pago'
        )

        total_atualizados = 0
        for aluno in alunos_vencidos:
            aluno.status_pagamento = 'Vencido'
            aluno.save()
            total_atualizados += 1
            self.stdout.write(self.style.WARNING(f'A assinatura de {aluno.nome_completo} foi atualizada para "Vencido".'))

        if total_atualizados > 0:
            self.stdout.write(self.style.SUCCESS(f'Operação concluída. Total de {total_atualizados} assinaturas atualizadas.'))
        else:
            self.stdout.write(self.style.SUCCESS('Nenhuma assinatura vencida encontrada para atualizar.'))