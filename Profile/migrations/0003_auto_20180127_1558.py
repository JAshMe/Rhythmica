# Generated by Django 2.0 on 2018-01-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_userprofile_dp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dp',
            field=models.ImageField(default='user_dp/anonymous.png', upload_to='user_dp', verbose_name='Profile Picture'),
        ),
    ]
