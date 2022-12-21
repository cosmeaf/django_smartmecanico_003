from django.db import models
from django.contrib.auth.models import User

from .base import Base;


class Address(Base, models.Model):
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    cep = models.CharField('Cep', max_length=10)
    logradouro = models.CharField('Logradouro', max_length=255, blank=False, null=False)
    complemento = models.CharField('Complemento', max_length=255, blank=False, null=False)
    bairro = models.CharField('Bairro', max_length=255, blank=False, null=False)
    localidade = models.CharField('Cidade', max_length=255, blank=False, null=False)
    uf = models.CharField('Estado', max_length=2,  blank=False, null=False, editable=True)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.cep}'