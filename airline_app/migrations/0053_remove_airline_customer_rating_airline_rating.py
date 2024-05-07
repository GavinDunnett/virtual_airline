# Generated by Django 5.0.2 on 2024-04-18 23:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_app', '0052_alter_airport_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airline',
            name='customer_rating',
        ),
        migrations.AddField(
            model_name='airline',
            name='rating',
            field=models.DecimalField(decimal_places=3, default=0.75, max_digits=4, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
    ]