# Generated by Django 2.2 on 2019-09-29 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_movie_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='rating',
        ),
        migrations.AddField(
            model_name='movie',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
    ]
