# Generated by Django 5.0 on 2024-05-01 04:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime(2024, 5, 1, 10, 10, 9, 927226))),
            ],
        ),
    ]
