from django.db import models
from django.contrib.auth.models import User
from api.models.base import Base

class Ipva(Base, models.Model):
    """Model definition for IPVA."""
    date = models.DateField('Data Pagamento', auto_now=False, auto_now_add=False)
    date = models.DateField('Data Vencimento', auto_now=False, auto_now_add=False)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)

    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for IPVA."""
        verbose_name = 'Ipva'
        verbose_name_plural = 'Ipvas'