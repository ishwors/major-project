# Generated by Django 4.2.2 on 2023-07-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_booking_payment_method_invoice_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='amount',
            field=models.FloatField(null=True),
        ),
    ]