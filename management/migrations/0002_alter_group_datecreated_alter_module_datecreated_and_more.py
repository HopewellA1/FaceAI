# Generated by Django 4.1.7 on 2023-10-06 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 9, 46, 56, 522989)),
        ),
        migrations.AlterField(
            model_name='module',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 9, 46, 56, 522989)),
        ),
        migrations.AlterField(
            model_name='program',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 9, 46, 56, 522989)),
        ),
    ]
