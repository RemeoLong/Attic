# Generated by Django 2.2.16 on 2021-04-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='', max_length=20, unique=True),
        ),
    ]