# Generated by Django 3.2.8 on 2021-10-11 22:04

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20211004_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipationApplicationFestival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('birthday', models.DateField(verbose_name='День рождения')),
                ('city', models.CharField(max_length=50, verbose_name='Город проживания')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=100, verbose_name='Электронная почта')),
                ('title', models.CharField(max_length=200, verbose_name='Название пьесы')),
                ('year', models.CharField(max_length=4, verbose_name='Год написания')),
                ('file_link', models.URLField(verbose_name='Ссылка на файл')),
                ('status', models.BooleanField(verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заявление на участие',
                'verbose_name_plural': 'Заявления на участие',
            },
        ),
    ]
