# Generated by Django 2.0 on 2018-01-28 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0007_auto_20180127_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dp',
            field=models.ImageField(default='/user_dp/anonymous.png', upload_to='user_dp', verbose_name='Profile Picture'),
        ),
    ]
