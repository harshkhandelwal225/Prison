# Generated by Django 2.2.5 on 2019-10-16 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_fir_release_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fir',
            name='release_date',
        ),
        migrations.AddField(
            model_name='fir',
            name='File_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 16, 18, 0, 32, 666456)),
        ),
    ]
