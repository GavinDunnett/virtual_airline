# Generated by Django 5.0.2 on 2024-04-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_app', '0009_fleet_next_d_check_alter_fleet_next_a_check_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='image',
            field=models.ImageField(default='default.png', upload_to='static/aircraft'),
        ),
    ]
