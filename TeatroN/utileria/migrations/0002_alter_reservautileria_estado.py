# Generated by Django 5.0.6 on 2024-07-01 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utileria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservautileria',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('aprobada', 'Aprobada'), ('denegada', 'Denegada')], default='pendiente', max_length=20),
        ),
    ]