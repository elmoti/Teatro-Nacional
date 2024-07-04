# Generated by Django 5.0.6 on 2024-07-03 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DirectorObra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_id', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('anos_experiencia', models.IntegerField()),
            ],
            options={
                'db_table': 'directores_obra',
            },
        ),
        migrations.CreateModel(
            name='Escenografo',
            fields=[
                ('ci', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('anios_experiencia', models.IntegerField()),
            ],
            options={
                'db_table': 'escenografos',
            },
        ),
        migrations.CreateModel(
            name='ObraTeatro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('genero', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
            options={
                'db_table': 'obras_teatro',
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('capacidad', models.IntegerField()),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'salas',
            },
        ),
        migrations.CreateModel(
            name='Utileria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'utileria',
            },
        ),
        migrations.CreateModel(
            name='Utilero',
            fields=[
                ('ci', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('anios_experiencia', models.IntegerField()),
            ],
            options={
                'db_table': 'utileros',
            },
        ),
        migrations.CreateModel(
            name='ReservaUtileria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_reserva', models.DateField()),
                ('fecha_aprobacion', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('aprobada', 'Aprobada'), ('denegada', 'Denegada')], default='pendiente', max_length=20)),
                ('director_obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utileria.directorobra')),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utileria.obrateatro')),
                ('utileria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utileria.utileria')),
            ],
            options={
                'db_table': 'reservas_utileria',
            },
        ),
        migrations.AddField(
            model_name='obrateatro',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utileria.sala'),
        ),
        migrations.CreateModel(
            name='Asiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fila', models.CharField(max_length=5)),
                ('numero', models.IntegerField()),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utileria.sala')),
            ],
            options={
                'db_table': 'asientos',
            },
        ),
        migrations.CreateModel(
            name='Supervision',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('escenografo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utileria.escenografo')),
                ('reserva', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='utileria.reservautileria')),
            ],
            options={
                'db_table': 'supervisiones',
            },
        ),
    ]
