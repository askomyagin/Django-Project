# Generated by Django 3.1.7 on 2021-03-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextSongs', '0004_albums_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='title_en',
            field=models.CharField(default='0000000', max_length=80),
        ),
    ]
