# Generated by Django 2.2 on 2019-11-22 18:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 18, 39, 59, 737013, tzinfo=utc)),
        ),
    ]
