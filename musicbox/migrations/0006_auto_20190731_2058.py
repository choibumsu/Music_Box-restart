# Generated by Django 2.2.3 on 2019-07-31 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbox', '0005_artist_another_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='another_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]