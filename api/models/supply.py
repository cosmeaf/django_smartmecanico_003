from django.db import models
from django.contrib.auth.models import User
from api.models.base import Base

class Supply(Base, models.Model):
    """Model definition for Supply."""
    date = models.DateField('Data Abastecimento', auto_now=False, auto_now_add=False)
    liter = models.DecimalField('Litros', max_digits=5, decimal_places=2)
    price = models.DecimalField('Preço', max_digits=5, decimal_places=2)
    kilometer = models.DecimalField('Kilometragem',default=000.000,  max_digits=6, decimal_places=3)
    total_expense = models.DecimalField("Total Gasto",default=0.00, max_digits=10, decimal_places=2, blank=True, null=True)
    total_liters = models.DecimalField("Total Litros",default=0.00,  max_digits=10, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for Supply."""
        verbose_name = 'Supply'
        verbose_name_plural = 'Supplies'