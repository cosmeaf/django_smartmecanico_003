# Generated by Django 4.1.4 on 2023-01-02 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_financing_price_alter_finetraffic_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finetraffic',
            old_name='poit',
            new_name='point',
        ),
    ]