# Generated by Django 4.0.2 on 2022-02-08 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kaszubnet_app', '0004_warehouse_warehouselog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Warehouse',
            new_name='WarehouseItems',
        ),
        migrations.AlterModelOptions(
            name='warehouseitems',
            options={'verbose_name': 'Przedmiot zmagazynowany', 'verbose_name_plural': 'Przedmioty zmagazynowane'},
        ),
        migrations.AlterModelOptions(
            name='warehouselog',
            options={'verbose_name': 'Ewidencja magazynowa', 'verbose_name_plural': 'Ewidencja magazynowa'},
        ),
    ]
