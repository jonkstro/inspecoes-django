# Generated by Django 4.1.3 on 2022-11-03 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0004_alter_planomanut_equipamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Validacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_inspec', models.BooleanField()),
                ('is_sap', models.BooleanField()),
                ('ordem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.planomanut')),
            ],
        ),
    ]
