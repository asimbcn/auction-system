# Generated by Django 3.1 on 2020-12-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_customer_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(null=True, upload_to='profile/'),
        ),
    ]
