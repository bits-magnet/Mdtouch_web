# Generated by Django 2.0.9 on 2018-12-12 06:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDTouch', '0009_auto_20181212_1216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='picurl',
            new_name='pic',
        ),
        migrations.AlterField(
            model_name='ambulancebilling',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 12, 12, 17, 14, 235165)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='qualification',
            field=models.ManyToManyField(to='MDTouch.Qualification'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.ManyToManyField(to='MDTouch.Specialization'),
        ),
    ]
