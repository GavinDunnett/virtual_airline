# Generated by Django 5.0.2 on 2024-04-24 14:29

import airline_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_app', '0098_alter_fleet_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleet',
            name='registration',
            field=models.CharField(default=airline_app.models.random_aircraft_registration_generator, help_text="A code unique to a single aircraft and\n      marked on the civil aircraft's exterior.", max_length=8),
        ),
    ]
