# Generated by Django 3.1 on 2020-12-24 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0036_auto_20201222_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 24, 21, 1, 49, 414096), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='valid_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 31, 21, 1, 49, 414096), null=True),
        ),
    ]
