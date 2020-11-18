# Generated by Django 3.1.1 on 2020-11-17 23:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marcas', models.CharField(choices=[('INTEL', 'INTEL'), ('AMD', 'AMD'), ('INTEL_AMD', 'INTEL E AMD')],
                                            max_length=100)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Tamanhos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanho', models.CharField(
                    choices=[('4 GB', '4 GB'), ('8 GB', '8 GB'), ('16 GB', '16 GB'), ('32 GB', '32 GB'),
                             ('64 GB', '64 GB')], max_length=100)),
            ],
            options={
                'verbose_name': 'Tamanho',
                'verbose_name_plural': 'Tamanhos',
            },
        ),
    ]
