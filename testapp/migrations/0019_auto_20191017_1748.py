# Generated by Django 2.2.5 on 2019-10-17 12:18

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0018_auto_20191017_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='allvisitors',
            name='date_of_visit',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 17, 17, 48, 26, 428454)),
        ),
        migrations.AlterField(
            model_name='fir',
            name='File_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 17, 17, 48, 26, 426459)),
        ),
        migrations.AlterField(
            model_name='prisoner',
            name='date_of_entry',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 17, 17, 48, 26, 427456)),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='date_of_visit',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 17, 17, 48, 26, 427456)),
        ),
    ]
