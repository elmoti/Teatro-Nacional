# Generated by Django 5.0.6 on 2024-07-01 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contrasena', models.CharField(max_length=255)),
                ('rol', models.CharField(max_length=50)),
            ],
        ),
    ]