# Generated by Django 3.1.6 on 2021-02-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210211_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
