# Generated by Django 2.2.5 on 2019-10-17 12:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0014_auto_20191017_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='allvisitors',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('visitor_aadhar_no', models.BigIntegerField(primary_key=True, serialize=False)),
                ('prisoner_aadhar_no', models.BigIntegerField()),
                ('date_of_visit', models.DateTimeField(default=datetime.datetime(2019, 10, 17, 17, 36, 16, 299468))),
            ],
        ),
        migrations.AlterField(
            model_name='fir',
            name='File_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 17, 17, 36, 16, 298471)),
        ),
        migrations.AlterField(
            model_name='prisoner',
            name='date_of_entry',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 17, 17, 36, 16, 298471)),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='date_of_visit',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 17, 17, 36, 16, 299468)),
        ),
    ]
