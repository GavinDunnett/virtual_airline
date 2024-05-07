# Generated by Django 5.0.2 on 2024-04-22 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_app', '0080_airline_current_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='homebase',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='airline_app.airport'),
        ),
    ]
