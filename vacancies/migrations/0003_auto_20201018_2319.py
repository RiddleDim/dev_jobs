# Generated by Django 3.1.2 on 2020-10-18 23:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_auto_20201018_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='published_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 18, 23, 19, 50, 289377, tzinfo=utc)),
        ),
    ]
