from django.db import models
from django.contrib.auth.models import User
from api.models.base import Base

class Financing(Base, models.Model):
    """Model definition for financing."""
    name = models.CharField("Nome Fiananceira", max_length=50)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for financing."""
        verbose_name = 'Financing'
        verbose_name_plural = 'Financing'



