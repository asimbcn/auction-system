# Generated by Django 3.1 on 2020-12-03 15:32

import autoslug.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0023_auto_20201203_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 3, 21, 17, 53, 419545), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='valid_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 10, 21, 17, 53, 419545), null=True),
        ),
    ]
