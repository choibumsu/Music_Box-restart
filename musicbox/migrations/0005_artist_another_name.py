# Generated by Django 2.2.3 on 2019-07-31 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0004_auto_20190731_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='another_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]