# Generated by Django 2.2.3 on 2019-08-16 14:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('ticket_url', models.URLField()),
                ('image', models.ImageField(upload_to='events/')),
                ('event_date', models.DateTimeField(default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Events',
            },
        ),
    ]