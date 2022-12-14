# Generated by Django 4.1.4 on 2023-01-02 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0011_financing'),
    ]

    operations = [
        migrations.CreateModel(
            name='FineTraffic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ultima Atualização')),
                ('deleted_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Exclusão')),
                ('date', models.DateField(verbose_name='Data da Multa')),
                ('number', models.IntegerField(verbose_name='Numero da Multa')),
                ('poit', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Numero de Ponto')),
                ('description', models.TextField(verbose_name='Observação')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço da Multa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'FineTraffic',
                'verbose_name_plural': 'FineTraffics',
            },
        ),
    ]
