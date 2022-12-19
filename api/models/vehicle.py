from django.db import models
from django.contrib.auth.models import User
from api.models.base import Base

class Vehicle(Base):
    """Model definition for Vehicle."""
    brand = models.CharField(
        'Marca Veículo', max_length=255, blank=False, null=False)
    model = models.CharField(
        'Modelo Veículo', max_length=255, blank=False, null=False)
    fuell = models.CharField(
        'Combustível', max_length=255, blank=False, null=False)
    year = models.CharField(
        'Ano Fabricação', max_length=4, blank=False, null=False)
    odomitter = models.CharField(
        'Hodometro', max_length=9, blank=False, null=False)
    plate = models.CharField(
        'Placa Veículo', max_length=10, blank=False, null=False)
    user = models.ForeignKey(
        User, verbose_name='Usuário', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Vehicle."""
        verbose_name = 'vehicle'
        verbose_name_plural = 'vehicles'

    def __str__(self):
        """Unicode representation of Vehicle."""
        return self.brand