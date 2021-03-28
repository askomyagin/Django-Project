# Generated by Django 3.1.7 on 2021-03-25 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TextSongs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albums',
            old_name='performer',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='albums',
            old_name='yearofcreated',
            new_name='year_of_created',
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation timestamp')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='TextSongs.albums')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TextSongs.performers')),
            ],
        ),
    ]
