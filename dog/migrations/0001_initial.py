# Generated by Django 3.0 on 2019-12-18 00:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('breed', models.CharField(max_length=200)),
                ('date_of_birth', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]