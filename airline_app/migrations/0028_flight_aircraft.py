# Generated by Django 5.0.2 on 2024-04-17 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_app', '0027_remove_flight_airline_designator_flight_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='aircraft',
            field=models.ForeignKey(default='', limit_choices_to={'airline': models.ForeignKey(default='XX XXXX', on_delete=django.db.models.deletion.CASCADE, to='airline_app.airline')}, on_delete=django.db.models.deletion.CASCADE, to='airline_app.fleet'),
        ),
    ]
