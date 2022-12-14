# Generated by Django 4.1.4 on 2023-01-08 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_finetraffic_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='end_kilometer',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=6, verbose_name='Km Retorno'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='start_kilometer',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=6, verbose_name='Km Saída'),
        ),
    ]
