from django.db import models
from django.contrib.auth.models import User
from api.models.base import Base

class Maintenance(Base, models.Model):
    """Model definition for Maintenance."""
    date = models.DateField('Data Manutenção', auto_now=False, auto_now_add=False)
    name = models.CharField('Tipo de Serviço',  max_length=100, blank=False, null=False)
    description = models.CharField("Descrição", max_length=100, blank=True, null=True)
    start_kilometer = models.DecimalField('Km Saída',default=000.000,  max_digits=6, decimal_places=3, blank=False, null=False)
    end_kilometer = models.DecimalField('Km Retorno',default=000.000,  max_digits=6, decimal_places=3, blank=False, null=False)
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for Maintenance."""
        verbose_name = 'Maintenance'
        verbose_name_plural = 'Maintenance'
    
    def __str__(self) -> str:
        return self.name