# Generated by Django 3.1 on 2020-11-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0002_auto_20201123_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='valid_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
