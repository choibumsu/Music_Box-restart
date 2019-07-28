# Generated by Django 2.2.3 on 2019-07-27 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('real_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a song gerne (e.g. Hiphop)', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(help_text='Enter a youtube video ID of this song', max_length=1000)),
                ('artist', models.ManyToManyField(to='musicbox.Artist')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='musicbox.Genre')),
            ],
            options={
                'ordering': ['title', 'genre'],
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('explanation', models.TextField(help_text='Enter a explanation of this song', max_length=1000)),
                ('songs', models.ManyToManyField(help_text='Select a songs for this playlist', to='musicbox.Song')),
            ],
        ),
    ]
