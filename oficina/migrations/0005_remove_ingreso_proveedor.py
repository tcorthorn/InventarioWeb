# Generated by Django 4.0.4 on 2022-07-21 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0004_alter_salida_destino_alter_sku_proveedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingreso',
            name='proveedor',
        ),
    ]