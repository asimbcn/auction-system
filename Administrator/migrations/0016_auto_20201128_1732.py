# Generated by Django 3.1 on 2020-11-28 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0015_auto_20201128_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='use_type',
            field=models.CharField(choices=[('Unlimited', 'Unlimited'), ('Onetime', 'Onetime')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 17, 32, 28, 276152), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='valid_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 5, 17, 32, 28, 276152), null=True),
        ),
    ]