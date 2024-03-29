# Generated by Django 3.1 on 2020-11-30 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0020_auto_20201130_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.IntegerField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 19, 51, 59, 818360), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='valid_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 7, 19, 51, 59, 818360), null=True),
        ),
    ]
