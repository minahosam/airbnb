# Generated by Django 3.1.1 on 2020-09-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb', '0003_auto_20200922_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='airbnb',
            name='duration',
            field=models.DurationField(default=''),
            preserve_default=False,
        ),
    ]