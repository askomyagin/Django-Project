# Generated by Django 3.1.7 on 2021-03-26 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextSongs', '0005_songs_title_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='performers',
            name='small_text',
            field=models.TextField(default=' '),
        ),
    ]
