# Generated by Django 5.0.2 on 2024-04-15 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_app', '0006_airline_designator_airline_homebase'),
    ]

    operations = [
        migrations.AddField(
            model_name='fleet',
            name='cycles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fleet',
            name='last_100_hour_inspection',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=16),
        ),
        migrations.AddField(
            model_name='fleet',
            name='last_a_check',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='fleet',
            name='last_b_check',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='fleet',
            name='last_c_check',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='fleet',
            name='last_engine_overhaul',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=16),
        ),
    ]
