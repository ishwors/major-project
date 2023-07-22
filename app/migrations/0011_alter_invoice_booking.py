# Generated by Django 4.2.2 on 2023-07-21 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_invoice_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='booking',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='app.booking'),
        ),
    ]