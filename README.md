# sendEmail
Maneira simples de enviar e-mail utilizando python + django

Adicione os seguintes comando no arquivo settings.py:

<pre>
#CONFIGURAÇÃO PARA ENVIAR EMAIL
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'usuario email'
EMAIL_HOST_PASSWORD = 'senha do email caso precise'
EMAIL_USE_TLS = True #se escolher essa opção como TRUE, deixe a de baixo como FALSE
EMAIL_USE_SSL = False #se escolher essa opção como TRUE, deixe a de cima como FALSE
</pre>

Logo após a inserção dos códigos acima, na sua 'views' do app que criou, adicione o seguinte código:

<pre>
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
    
</pre>
