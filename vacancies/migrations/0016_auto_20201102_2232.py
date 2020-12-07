# Generated by Django 3.1.2 on 2020-11-02 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0015_auto_20201101_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='written_username',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='resume',
            name='education',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='resume',
            name='grade',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='resume',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='resume',
            name='portfolio',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='resume',
            name='specialty',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='resume',
            name='status',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='resume',
            name='surname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]