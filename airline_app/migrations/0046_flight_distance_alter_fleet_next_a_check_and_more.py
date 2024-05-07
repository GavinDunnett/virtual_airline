# Generated by Django 5.0.2 on 2024-04-18 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_app', '0045_flight_rating_alter_flight_act_arrival_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='distance',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='fleet',
            name='next_a_check',
            field=models.DateField(default=datetime.date(2024, 6, 27)),
        ),
        migrations.AlterField(
            model_name='fleet',
            name='next_b_check',
            field=models.DateField(default=datetime.date(2025, 1, 23)),
        ),
        migrations.AlterField(
            model_name='fleet',
            name='next_c_check',
            field=models.DateField(default=datetime.date(2025, 10, 30)),
        ),
        migrations.AlterField(
            model_name='fleet',
            name='next_d_check',
            field=models.DateField(default=datetime.date(2031, 12, 18)),
        ),
    ]
