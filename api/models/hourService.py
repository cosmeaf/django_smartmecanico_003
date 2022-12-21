from django.db import models
from django.contrib.auth.models import User
from api.models.base import Base


class HourService(Base, models.Model):
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE, related_name='hour_service')
    hour = models.CharField('Hora Serviço', max_length=8)

    class Meta:
        verbose_name = 'Hour Service'
        verbose_name_plural = 'Hour Services'

    def __str__(self):
        return f'{self.hour}'