# Generated by Django 3.2.9 on 2023-07-07 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20230628_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('review_text', models.TextField(max_length=150)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
            ],
        ),
    ]
