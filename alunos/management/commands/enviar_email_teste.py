from django.core.management.base import BaseCommand
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Envia um e-mail de teste para verificar a configuração de e-mail.'

    def handle(self, *args, **options):
        self.stdout.write("Tentando enviar um e-mail de teste...")
        try:
            send_mail(
                'Assunto do E-mail de Teste',
                'Olá! Este é o corpo da mensagem de teste.',
                'remetente@teste.com',
                ['destinatario@teste.com'],
                fail_silently=False,
            )
            self.stdout.write(self.style.SUCCESS("E-mail enviado para o console com sucesso! Verifique o terminal."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Falha ao enviar e-mail: {e}"))