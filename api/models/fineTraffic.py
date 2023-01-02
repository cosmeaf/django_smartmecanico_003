from django.db import models
from django.contrib.auth.models import User
from api.models.base import Base

class FineTraffic(Base, models.Model):
    """Model definition for Fine Traffic."""
    date = models.DateField('Data da Multa', auto_now=False, auto_now_add=False)
    number = models.IntegerField("Numero da Multa")
    point = models.DecimalField('Numero de Ponto', max_digits=2, decimal_places=0, null=False, blank=False)
    description = models.TextField("Observação", null=False, blank=False)
    price = models.DecimalField('Preço da Multa', max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for Fine Traffic.."""
        verbose_name = 'FineTraffic'
        verbose_name_plural = 'FineTraffics'
    



