# Generated by Django 2.2 on 2019-08-07 04:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicmodels', '0006_auto_20190807_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postreferrals',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 7, 12, 47, 20, 547574)),
        ),
        migrations.AlterField(
            model_name='visits',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 7, 12, 47, 20, 545579)),
        ),
    ]
