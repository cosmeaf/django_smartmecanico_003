from rest_framework.views import APIView
from django.conf import settings
from django.core.mail import send_mass_mail
from rest_framework.response import Response
from django.http import HttpResponse  


class EmailAPI(APIView):
    datatuple = (
        ('SMART MECÂNICO - TESTE E-MAIL FROM API', 
         'Teste de Envio de E-mail da API Smart Mecânico.', 
         settings.EMAIL_HOST_USER, 
         ['cosme.alex@gmail.com']),
        ('SMART MECÂNICO - TESTE E-MAIL FROM API', 
         'Teste de Envio de E-mail da API Smart Mecânico..', 
         settings.EMAIL_HOST_USER, 
         ['Jamersonrn@gmail.com ']),
    )
    send_mass_mail(datatuple)