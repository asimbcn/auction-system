# Generated by Django 3.1 on 2020-12-19 07:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0027_auto_20201219_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 19, 13, 40, 16, 747555), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='valid_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 26, 13, 40, 16, 747555), null=True),
        ),
    ]