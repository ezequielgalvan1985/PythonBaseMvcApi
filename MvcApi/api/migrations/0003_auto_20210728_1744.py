# Generated by Django 3.2.5 on 2021-07-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210728_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='horaentregado',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Hora Entregado'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='horarecepcion',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Hora Recepcion'),
        ),
    ]