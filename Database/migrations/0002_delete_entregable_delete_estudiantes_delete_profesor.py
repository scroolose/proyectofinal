# Generated by Django 4.1 on 2022-08-16 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiantes',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
