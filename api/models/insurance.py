from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from api.models.base import Base

class Insurance(Base, models.Model):
    """Model definition for vehicle_insurance."""
    name = models.CharField("Nome Seguradora", max_length=50)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    due_date=models.CharField('Data Vencimento', max_length=10, null=True, blank=True)
    policy = models.CharField("Numero Apolice:", max_length=100, null=True, blank=True)
    broker_name = models.CharField("Nome Corretora", max_length=50, null=True, blank=True)
    agent_name = models.CharField("Nome Agente", max_length=50, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,20}$', message="Phone number must be entered in the format: '00 00 9 9999 9999'. Up to 15 digits allowed.")
    phone_number = models.CharField('Contato', validators=[phone_regex],max_length=17, blank=True, null=True)
    email = models.EmailField("E-mail", max_length=254, null=True, blank=True)
    url = models.URLField("Site", max_length=254, null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for vehicle_insurance."""
        verbose_name = 'Insurance'
        verbose_name_plural = 'Insurances'



