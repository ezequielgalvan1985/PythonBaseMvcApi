# Generated by Django 3.2.5 on 2021-08-03 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210803_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidadmedida',
            name='abreviatura',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Abreviatura'),
        ),
    ]