# Generated by Django 5.0.2 on 2024-04-19 23:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_app', '0064_alter_flight_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='aircraft',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='airline_app.fleet'),
        ),
    ]
