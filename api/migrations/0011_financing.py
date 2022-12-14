# Generated by Django 4.1.4 on 2023-01-02 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_insurance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Financing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ultima Atualização')),
                ('deleted_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Exclusão')),
                ('name', models.CharField(max_length=50, verbose_name='Nome Fiananceira')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Financing',
                'verbose_name_plural': 'Financing',
            },
        ),
    ]
