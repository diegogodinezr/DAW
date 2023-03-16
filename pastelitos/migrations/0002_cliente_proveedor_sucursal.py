# Generated by Django 3.2.3 on 2023-03-15 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastelitos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=20)),
                ('apellido', models.CharField(default=None, max_length=70)),
                ('codigo_postal', models.IntegerField()),
                ('calle', models.CharField(default=None, max_length=100)),
                ('colonia', models.CharField(default=None, max_length=100)),
                ('num_ext', models.IntegerField()),
                ('num_int', models.IntegerField()),
                ('estado', models.CharField(default=None, max_length=20)),
                ('ciudad', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(default=None, max_length=70)),
                ('codigo_postal', models.IntegerField()),
                ('calle', models.CharField(default=None, max_length=100)),
                ('colonia', models.CharField(default=None, max_length=100)),
                ('num_ext', models.IntegerField()),
                ('num_int', models.IntegerField()),
                ('estado', models.CharField(default=None, max_length=20)),
                ('ciudad', models.CharField(default=None, max_length=50)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_postal', models.IntegerField()),
                ('calle', models.CharField(default=None, max_length=100)),
                ('colonia', models.CharField(default=None, max_length=100)),
                ('num_ext', models.IntegerField()),
                ('num_int', models.IntegerField()),
                ('estado', models.CharField(default=None, max_length=20)),
                ('ciudad', models.CharField(default=None, max_length=50)),
                ('telefono', models.IntegerField()),
            ],
        ),
    ]
