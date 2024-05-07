# Generated by Django 5.0.2 on 2024-04-24 15:26

import airline_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_app', '0103_alter_fleet_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleet',
            name='registration',
            field=models.CharField(default=airline_app.models.random_aircraft_registration_generator, help_text="<br>A code unique to a single aircraft and\n      marked on it's exterior.", max_length=8),
        ),
    ]