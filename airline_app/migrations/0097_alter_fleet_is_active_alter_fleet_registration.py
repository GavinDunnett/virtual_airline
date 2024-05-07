# Generated by Django 5.0.2 on 2024-04-24 14:25

import airline_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_app', '0096_alter_fleet_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleet',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this fleet aircraft should be treated as active.\n        Uncheck instead of deleting fleet aircarft.', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='fleet',
            name='registration',
            field=models.CharField(default=airline_app.models.random_aircraft_registration_generator, help_text='A code unique to a single aircraft,\n      marked on the exterior of every civil aircraft.\n      Leave blank to have one automatically assigned on saving.', max_length=8),
        ),
    ]