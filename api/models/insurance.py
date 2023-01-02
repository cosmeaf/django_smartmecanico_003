from django.db import models
from django.contrib.auth.models import User
from api.models.base import Base

class Insurance(Base, models.Model):
    """Model definition for vehicle_insurance."""
    name = models.CharField("Nome Seguradora", max_length=50)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for vehicle_insurance."""
        verbose_name = 'Insurance'
        verbose_name_plural = 'Insurances'



