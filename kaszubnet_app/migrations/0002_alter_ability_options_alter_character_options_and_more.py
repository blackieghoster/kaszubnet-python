# Generated by Django 4.0.2 on 2022-02-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaszubnet_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ability',
            options={'verbose_name': 'Umiejętność', 'verbose_name_plural': 'Umiejętności'},
        ),
        migrations.AlterModelOptions(
            name='character',
            options={'verbose_name': 'Postać', 'verbose_name_plural': 'Postaci'},
        ),
        migrations.AlterField(
            model_name='character',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
