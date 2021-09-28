# Generated by Django 3.2.7 on 2021-09-28 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20210922_2258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='performancemediareview',
            options={'ordering': ('-created',), 'verbose_name': 'Медиа отзыв на спектакль', 'verbose_name_plural': 'Медиа отзывы на спектакль'},
        ),
        migrations.AlterModelOptions(
            name='performancereview',
            options={'ordering': ('-created',), 'verbose_name': 'Отзыв зрителя на спектакль', 'verbose_name_plural': 'Отзывы зрителей на спектакль'},
        ),
        migrations.AddField(
            model_name='performancemediareview',
            name='image',
            field=models.ImageField(default=1, upload_to='reviews/', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performancemediareview',
            name='media_name',
            field=models.CharField(default=123, max_length=100, verbose_name='Название медиа ресурса'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performancemediareview',
            name='performance',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.PROTECT, related_name='media_reviews', to='library.performance', verbose_name='Спектакль'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performancemediareview',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=31232, verbose_name='Дата публикации'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performancemediareview',
            name='url',
            field=models.URLField(blank=True, verbose_name='Ссылка на отзыв'),
        ),
        migrations.AddField(
            model_name='performancereview',
            name='name',
            field=models.CharField(default=234124, max_length=100, verbose_name='Имя зрителя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performancereview',
            name='performance',
            field=models.ForeignKey(default=312313, on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='library.performance', verbose_name='Спектакль'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performancereview',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=123123, verbose_name='Дата публикации'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performancereview',
            name='url',
            field=models.URLField(blank=True, verbose_name='Ссылка на отзыв'),
        ),
        migrations.AlterField(
            model_name='performancemediareview',
            name='text',
            field=models.TextField(max_length=500, verbose_name='Текст отзыва'),
        ),
        migrations.AlterField(
            model_name='performancereview',
            name='text',
            field=models.TextField(max_length=500, verbose_name='Текст отзыва'),
        ),
    ]
