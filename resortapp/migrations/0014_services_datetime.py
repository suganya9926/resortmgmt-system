# Generated by Django 4.0.4 on 2022-05-18 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resortapp', '0013_payments_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
    ]