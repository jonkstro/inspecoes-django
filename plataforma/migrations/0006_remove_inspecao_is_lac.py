# Generated by Django 4.1.3 on 2022-11-08 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0005_validacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inspecao',
            name='is_lac',
        ),
    ]