# Generated by Django 3.2.3 on 2023-03-29 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ropa', '0003_alter_producto_r_descuento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto_r',
            name='descuento',
        ),
    ]
