# Generated by Django 3.1.2 on 2020-10-22 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0006_auto_20201022_2020'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Appliction',
            new_name='Application',
        ),
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
