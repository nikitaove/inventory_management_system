# Generated by Django 3.2.4 on 2022-07-22 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='inventory',
            table='inventory',
        ),
        migrations.AlterModelTable(
            name='supplier',
            table='supplier',
        ),
    ]
