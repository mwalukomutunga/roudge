# Generated by Django 2.2.3 on 2019-08-16 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='active',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
