# Generated by Django 3.1 on 2020-12-20 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0028_auto_20201219_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateField(default=datetime.date(2020, 12, 20), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='valid_time',
            field=models.DateField(default=datetime.date(2020, 12, 28), null=True),
        ),
    ]
