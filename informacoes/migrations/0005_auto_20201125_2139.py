# Generated by Django 3.1.1 on 2020-11-26 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informacoes', '0004_auto_20201125_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marcas',
            name='marcas',
            field=models.CharField(choices=[('INTEL', 'INTEL'), ('AMD', 'AMD'), ('INTEL E AMD', 'INTEL E AMD')], max_length=100),
        ),
    ]