# Generated by Django 4.0.4 on 2022-06-05 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salida',
            name='destino',
            field=models.CharField(blank=True, choices=[('wareclouds', 'Wareclouds'), ('casamoda', 'Casa Moda'), ('aura', 'Aura'), ('enviodirecto', 'Envio directo'), ('otro', 'Otro')], max_length=20),
        ),
    ]