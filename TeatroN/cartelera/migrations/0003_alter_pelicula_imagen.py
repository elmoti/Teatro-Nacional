# Generated by Django 5.0.6 on 2024-07-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartelera', '0002_pelicula_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]