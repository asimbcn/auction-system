# Generated by Django 3.1 on 2020-11-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0005_auto_20201123_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='valid_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]