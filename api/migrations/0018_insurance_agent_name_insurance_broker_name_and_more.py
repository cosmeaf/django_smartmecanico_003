# Generated by Django 4.1.4 on 2023-01-06 16:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_maintenance_description_alter_maintenance_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurance',
            name='agent_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome Agente'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='broker_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome Corretora'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data Vencimento'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '00 00 9 9999 9999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,20}$')], verbose_name='Contato'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='policy',
            field=models.IntegerField(blank=True, null=True, verbose_name='Numero Apolice:'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Site'),
        ),
    ]