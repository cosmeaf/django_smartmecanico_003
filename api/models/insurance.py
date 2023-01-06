from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from api.models.base import Base

class Insurance(Base, models.Model):
    """Model definition for vehicle_insurance."""
    name = models.CharField("Nome Seguradora", max_length=50)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    due_date=models.DateField('Data Vencimento',auto_now=False, null=True, blank=True)
    policy = models.IntegerField("Numero Apolice:", null=True, blank=True)
    broker_name = models.CharField("Nome Corretora", max_length=50, null=True, blank=True)
    agent_name = models.CharField("Nome Agente", max_length=50, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,20}$', message="Phone number must be entered in the format: '00 00 9 9999 9999'. Up to 15 digits allowed.")
    phone_number = models.IntegerField('Contato', validators=[phone_regex], blank=True, null=True)
    email = models.EmailField("E-mail", max_length=254, null=True, blank=True)
    url = models.URLField("Site", max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for vehicle_insurance."""
        verbose_name = 'Insurance'
        verbose_name_plural = 'Insurances'



