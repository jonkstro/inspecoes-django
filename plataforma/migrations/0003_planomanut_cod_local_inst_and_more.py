# Generated by Django 4.1.3 on 2022-11-03 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0002_rename_subestacao_planomanut_local_inst'),
    ]

    operations = [
        migrations.AddField(
            model_name='planomanut',
            name='cod_local_inst',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='planomanut',
            name='local_inst',
            field=models.CharField(max_length=50),
        ),
    ]
