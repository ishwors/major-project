# Generated by Django 3.2.9 on 2023-07-18 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_booking_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='timing',
        ),
    ]