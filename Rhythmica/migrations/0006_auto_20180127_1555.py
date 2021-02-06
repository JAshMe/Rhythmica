# Generated by Django 2.0 on 2018-01-27 10:25

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rhythmica', '0005_auto_20180127_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='albumLogo',
            field=models.ImageField(default='I:/media//song_logos/anonymous.jpg', storage=django.core.files.storage.FileSystemStorage(location='I:/media/'), upload_to='album_logos', verbose_name='Album Logo'),
        ),
        migrations.AlterField(
            model_name='song',
            name='songLogo',
            field=models.ImageField(default='I:/media//song_logos/anonymous.jpg', storage=django.core.files.storage.FileSystemStorage(location='I:/media/'), upload_to='song_logos', verbose_name='Choose Logo'),
        ),
        migrations.AlterField(
            model_name='song',
            name='songUrl',
            field=models.FileField(upload_to='songs', verbose_name='Choose Song'),
        ),
    ]