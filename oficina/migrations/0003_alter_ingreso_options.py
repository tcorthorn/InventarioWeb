# Generated by Django 4.0.4 on 2022-07-08 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0002_alter_ingreso_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingreso',
            options={'ordering': ['-creado']},
        ),
    ]
