# Generated by Django 2.2.3 on 2019-07-31 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='name',
        ),
    ]
