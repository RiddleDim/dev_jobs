# Generated by Django 3.1.2 on 2020-11-01 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0014_auto_20201101_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='resume', to=settings.AUTH_USER_MODEL),
        ),
    ]
