from django.db import models
from django.contrib.auth.models import User
from api.models.base import Base

class FineTraffic(Base, models.Model):
    """Model definition for Fine Traffic."""
    date = models.CharField('Data da Multa', max_length=10, null=True, blank=True)
    number = models.CharField("Numero da Multa", max_length=10, null=True, blank=True)
    point = models.CharField('Numero de Ponto', max_length=2, null=True, blank=True)
    description = models.TextField("Observação", max_length=200, null=True, blank=True)
    price = models.DecimalField('Preço da Multa', max_digits=10, decimal_places=2, null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for Fine Traffic.."""
        verbose_name = 'FineTraffic'
        verbose_name_plural = 'FineTraffics'
    



