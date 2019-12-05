from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail #importamos o módulo para enviarmos email

def index(request):
    template_name = 'index.html'

    send_mail(
        'título para um email de teste',
        'essa mensagem é para identificar um email de teste',
        'emails de quem vai enviar',
        ['email de quem vai receber'],
        fail_silently=False
    )

    return render(request, template_name)