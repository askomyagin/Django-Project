# Generated by Django 3.1.7 on 2021-03-26 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextSongs', '0007_ordertext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertext',
            name='info',
            field=models.TextField(null=True),
        ),
    ]