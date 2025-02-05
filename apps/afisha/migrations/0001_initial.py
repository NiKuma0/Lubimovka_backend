# Generated by Django 3.2.11 on 2022-01-29 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Базовое событие',
                'verbose_name_plural': 'Базовые события',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(blank=True, choices=[('PERFORMANCE', 'Спектакль'), ('MASTERCLASS', 'Мастер-класс'), ('READING', 'Читка')], max_length=50, verbose_name='Тип события')),
                ('date_time', models.DateTimeField(verbose_name='Дата и время')),
                ('paid', models.BooleanField(default=False, verbose_name='Платное')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('place', models.CharField(max_length=200, verbose_name='Место')),
                ('pinned_on_main', models.BooleanField(default=False, verbose_name='Закрепить на главной')),
                ('common_event', models.ForeignKey(help_text='Создайте спектакль, читку или мастер-класс чтобы получить возможность создать соответствующее событие', on_delete=django.db.models.deletion.CASCADE, related_name='body', to='afisha.commonevent', verbose_name='Событие')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
                'ordering': ('-date_time',),
            },
        ),
    ]
