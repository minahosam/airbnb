# Generated by Django 3.1.1 on 2020-09-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb', '0006_auto_20200922_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airbnb',
            name='ROOM_STATUES',
            field=models.CharField(choices=[('single', 'single'), ('double', 'double')], max_length=20),
        ),
        migrations.AlterField(
            model_name='airbnb',
            name='SMOKING_CHOICES',
            field=models.CharField(choices=[('smoke', 'smoke'), ('not smoke', 'not smoke')], max_length=20),
        ),
    ]
