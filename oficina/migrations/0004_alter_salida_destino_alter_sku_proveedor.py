# Generated by Django 4.0.4 on 2022-07-20 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0003_alter_ingreso_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salida',
            name='destino',
            field=models.CharField(choices=[('packco', 'Packco'), ('casamoda', 'CasaModa'), ('aura', 'Aura'), ('enviodirecto', 'EnvioDirecto'), ('otro', 'Otro')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sku',
            name='proveedor',
            field=models.ForeignKey(blank=True, default='Otro', null=True, on_delete=django.db.models.deletion.SET_NULL, to='oficina.proveedor'),
        ),
    ]
