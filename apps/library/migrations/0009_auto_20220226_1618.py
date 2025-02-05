# Generated by Django 3.2.12 on 2022-02-26 13:18

import apps.library.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20220226_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='play',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[apps.library.validators.year_validator], verbose_name='Год написания пьесы'),
        ),
    ]
