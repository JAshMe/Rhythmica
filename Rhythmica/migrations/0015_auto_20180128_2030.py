# Generated by Django 2.0 on 2018-01-28 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rhythmica', '0014_auto_20180128_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='songLogo',
            field=models.ImageField(default='/song_logos/anonymous1.jpg', upload_to='song_logos', verbose_name='Choose Logo'),
        ),
    ]