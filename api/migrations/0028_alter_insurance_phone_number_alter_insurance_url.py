# Generated by Django 4.1.4 on 2023-01-08 01:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_alter_maintenance_end_kilometer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '00 00 9 9999 9999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,20}$')], verbose_name='Contato'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='url',
            field=models.URLField(blank=True, max_length=254, null=True, verbose_name='Site'),
        ),
    ]
