# Generated by Django 2.2 on 2019-09-22 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
