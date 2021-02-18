# Generated by Django 3.1.6 on 2021-02-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('myapp', '0002_auto_20210211_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='groups',
        ),
        migrations.AddField(
            model_name='role',
            name='groups',
            field=models.ManyToManyField(to='auth.Permission'),
        ),
    ]
