# Generated by Django 3.1 on 2020-11-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
