# Generated by Django 3.2.9 on 2023-06-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_patient_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='profile_pic',
            field=models.ImageField(default='client-assets\\img\\patients\\default.png', null=True, upload_to=''),
        ),
    ]
