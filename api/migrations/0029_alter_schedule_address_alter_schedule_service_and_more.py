# Generated by Django 4.1.4 on 2023-01-09 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_alter_insurance_phone_number_alter_insurance_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Address', related_query_name='Addres', to='api.address', verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Service', related_query_name='Service', to='api.service', verbose_name='Serviço'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vehicle', related_query_name='Vehicle', to='api.vehicle', verbose_name='Veículo'),
        ),
    ]