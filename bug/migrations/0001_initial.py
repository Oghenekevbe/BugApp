# Generated by Django 4.2.5 on 2023-10-03 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('bug_type', models.CharField(max_length=225)),
                ('report_date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('new', 'New'), ('assigned', 'Assigned'), ('in_progress', 'In Progress'), ('resolved', 'Resolved'), ('closed', 'Closed'), ('reopened', 'Reopened'), ('duplicate', 'Duplicate'), ('invalid', 'Invalid'), ('wont_fix', "Won't Fix")], max_length=50, unique=True)),
            ],
        ),
    ]