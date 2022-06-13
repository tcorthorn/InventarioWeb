# Generated by Django 4.0.4 on 2022-06-13 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateField(auto_now_add=True)),
                ('nombre', models.CharField(blank=True, default='Otro', max_length=10, null=True)),
                ('comentario', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateField(auto_now_add=True)),
                ('codigo', models.CharField(max_length=7, unique=True)),
                ('categoria', models.CharField(max_length=20)),
                ('producto', models.CharField(max_length=100)),
                ('comentario', models.CharField(blank=True, max_length=200, null=True)),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oficina.proveedor')),
            ],
            options={
                'ordering': ['categoria', 'producto'],
            },
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
                ('destino', models.CharField(blank=True, choices=[('wareclouds', 'Wareclouds'), ('casamoda', 'CasaModa'), ('aura', 'Aura'), ('enviodirecto', 'EnvioDirecto'), ('otro', 'Otro')], max_length=20)),
                ('comentario', models.CharField(blank=True, max_length=300, null=True)),
                ('sku', models.ManyToManyField(to='oficina.sku')),
            ],
            options={
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
                ('comentario', models.CharField(blank=True, default='Comentario', max_length=200, null=True)),
                ('proveedor', models.ManyToManyField(to='oficina.proveedor')),
                ('sku', models.ManyToManyField(to='oficina.sku')),
            ],
            options={
                'ordering': ['-creado'],
            },
        ),
    ]
