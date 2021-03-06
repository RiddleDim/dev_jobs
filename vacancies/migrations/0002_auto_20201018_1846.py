# Generated by Django 3.1.2 on 2020-10-18 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='published_at',
            field=models.DateField(default=datetime.date(2020, 10, 18)),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='skills',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
