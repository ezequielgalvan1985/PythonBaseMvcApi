# Generated by Django 3.2.5 on 2021-08-04 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20210804_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='googlemaps',
        ),
    ]