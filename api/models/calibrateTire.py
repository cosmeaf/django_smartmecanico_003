from django.db import models
from django.contrib.auth.models import User
from api.models.base import Base

class CalibrateTire(Base, models.Model):
    """Model definition for calibrate tire."""
    date = models.DateField('Ultima Calibragem', auto_now=False, auto_now_add=False)
    libra = models.CharField("Libra", max_length=2, blank=False, null=False )
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for calibrate tire."""
        verbose_name = 'CalibrateTire'
        verbose_name_plural = 'CalibrateTires'
    def __str__(self):
        return self.libra
    