# Generated by Django 5.0.2 on 2024-04-17 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airline_app', '0033_remove_flight_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='aircraft',
        ),
    ]
