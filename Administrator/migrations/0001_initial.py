# Generated by Django 3.1 on 2020-11-22 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('start_bid', models.IntegerField(blank=True, null=True)),
                ('max_bid', models.IntegerField(blank=True, null=True)),
                ('digital', models.BooleanField(default=False, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('status', models.BooleanField(default=False, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('valid_time', models.DateTimeField(blank=True, null=True)),
                ('seller', models.CharField(max_length=200, null=True)),
                ('condition', models.CharField(max_length=200, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
