# Generated by Django 3.1 on 2020-11-28 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0018_auto_20201128_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 17, 47, 29, 340273), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='valid_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 5, 17, 47, 29, 340273), null=True),
        ),
    ]