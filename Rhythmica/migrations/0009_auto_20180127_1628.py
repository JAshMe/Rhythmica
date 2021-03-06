# Generated by Django 2.0 on 2018-01-27 10:58

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rhythmica', '0008_auto_20180127_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='albumLogo',
            field=models.ImageField(default='I:\\Projects\\Python\\Django\\myWeb\\mediasong_logos/anonymous.jpg', storage=django.core.files.storage.FileSystemStorage(location='I:\\Projects\\Python\\Django\\myWeb\\media'), upload_to='album_logos', verbose_name='Album Logo'),
        ),
        migrations.AlterField(
            model_name='song',
            name='songLogo',
            field=models.ImageField(default='I:\\Projects\\Python\\Django\\myWeb\\mediasong_logos/anonymous.jpg', storage=django.core.files.storage.FileSystemStorage(location='I:\\Projects\\Python\\Django\\myWeb\\media'), upload_to='song_logos', verbose_name='Choose Logo'),
        ),
    ]
