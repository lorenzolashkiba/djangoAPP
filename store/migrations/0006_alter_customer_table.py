# Generated by Django 4.0.4 on 2022-05-19 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_address_zip'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='store_customers',
        ),
    ]
