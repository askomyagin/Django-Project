# Generated by Django 3.1.7 on 2021-03-25 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextSongs', '0002_auto_20210325_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='performers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
