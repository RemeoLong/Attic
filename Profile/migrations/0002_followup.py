# Generated by Django 2.2.16 on 2021-04-15 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='')),
                ('time', models.TimeField(default='')),
                ('comment', models.CharField(default='', max_length=150)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Working', 'Working'), ('Pending', 'Pending'), ('Complete', 'Complete')], default='Open', max_length=10)),
                ('profile', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Profile.Profile')),
            ],
        ),
    ]
