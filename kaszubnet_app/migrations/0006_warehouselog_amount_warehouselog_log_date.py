# Generated by Django 4.0.2 on 2022-02-08 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaszubnet_app', '0005_rename_warehouse_warehouseitems_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouselog',
            name='amount',
            field=models.IntegerField(null=True, verbose_name='Ilość'),
        ),
        migrations.AddField(
            model_name='warehouselog',
            name='log_date',
            field=models.DateTimeField(null=True),
        ),
    ]
