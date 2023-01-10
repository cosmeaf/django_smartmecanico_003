from django.db import models
from api.models.base import Base
from api.models.address import Address
from api.models.vehicle import Vehicle
from api.models.service import Service
from api.models.hourService import HourService
from django.contrib.auth.models import User


class Schedule(Base, models.Model):
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    address = models.ForeignKey(Address, verbose_name='Endereço', on_delete=models.CASCADE, related_name='Address', related_query_name="Addres")
    vehicle = models.ForeignKey(Vehicle, verbose_name='Veículo', on_delete=models.CASCADE, related_name='Vehicle', related_query_name="Vehicle")
    service = models.ForeignKey(Service, verbose_name='Serviço', on_delete=models.CASCADE, related_name='Service', related_query_name="Service")
    hour = models.CharField('Hora do Serviço', max_length=5)
    day = models.DateField('Data do Serviço', help_text='Escolha data disponível')

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'

    def __str__(self):
        return f'{self.service}'