# Generated by Django 5.0.6 on 2024-07-06 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartelera', '0006_alter_pelicula_imagen'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ObraSala',
        ),
    ]
