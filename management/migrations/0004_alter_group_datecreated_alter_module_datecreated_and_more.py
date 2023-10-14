# Generated by Django 4.1.7 on 2023-10-06 08:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0003_alter_group_datecreated_alter_module_datecreated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 10, 22, 34, 555525)),
        ),
        migrations.AlterField(
            model_name='module',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 10, 22, 34, 555525)),
        ),
        migrations.AlterField(
            model_name='program',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 10, 22, 34, 555525)),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
