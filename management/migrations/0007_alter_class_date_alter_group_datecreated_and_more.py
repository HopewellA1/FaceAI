# Generated by Django 4.1.7 on 2023-10-10 13:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_class_date_class_status_alter_group_datecreated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 10, 15, 55, 12, 315771)),
        ),
        migrations.AlterField(
            model_name='group',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 10, 15, 55, 12, 299774)),
        ),
        migrations.AlterField(
            model_name='module',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 10, 15, 55, 12, 299774)),
        ),
        migrations.AlterField(
            model_name='program',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 10, 15, 55, 12, 299774)),
        ),
        migrations.CreateModel(
            name='currentAttendee',
            fields=[
                ('currentAttendee', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Message', models.TextField(blank=True, null=True)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.class')),
                ('Student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.student')),
            ],
        ),
    ]
