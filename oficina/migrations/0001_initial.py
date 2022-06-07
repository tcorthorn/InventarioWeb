# Generated by Django 4.0.4 on 2022-06-05 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='Otro', max_length=10, null=True)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('sku', models.CharField(max_length=7)),
                ('cantidad', models.IntegerField()),
                ('destino', models.CharField(blank=True, choices=[('wareclouds', 'Wareclouds'), ('casamoda', 'Casamoda'), ('aura', 'Aura'), ('enviodirecto', 'Envio directo'), ('otro', 'Otro')], max_length=20)),
                ('comentario', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('sku', models.CharField(max_length=7)),
                ('cantidad', models.IntegerField()),
                ('comentario', models.CharField(max_length=200)),
                ('proveedor', models.ManyToManyField(to='oficina.proveedor')),
            ],
            options={
                'ordering': ['-fecha'],
            },
        ),
    ]
