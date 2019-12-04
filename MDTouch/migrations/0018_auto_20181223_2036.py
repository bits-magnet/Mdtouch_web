# Generated by Django 2.0.9 on 2018-12-23 15:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MDTouch', '0017_auto_20181223_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='notice',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MDTouch.Login'),
        ),
        migrations.AlterField(
            model_name='ambulancebilling',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 23, 20, 36, 57, 798033)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='qualification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MDTouch.Qualification'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MDTouch.Specialization'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 23, 20, 36, 57, 800119)),
        ),
    ]
