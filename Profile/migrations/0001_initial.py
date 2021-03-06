# Generated by Django 2.2.16 on 2021-04-29 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('service_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=25)),
                ('zip_code', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('services', models.CharField(choices=[('Pest: Mice', 'Pest: Mice'), ('Pest: Rats', 'Pest: Rats'), ('Pest: Racoons', 'Pest: Racoons'), ('Pest: Squirrels', 'Pest: Squirrels'), ('Pest: Skunks', 'Pest: Skunks'), ('Pest: Opossums', 'Pest: Opossums'), ('Pest: Snakes', 'Pest: Snakes'), ('Pest: Bats', 'Pest: Bats'), ('Pest: Birds', 'Pest: Birds'), ('Construction', 'Construction'), ('Roofing Repair', 'Roofing Repair'), ('Insulation Install', 'Insulation Install'), ('Sheet Rock', 'Sheet Rock'), ('Cement Small Jobs', 'Cement Small Jobs')], default='', max_length=50)),
                ('additional_service', models.CharField(blank=True, choices=[('Pest: Mice', 'Pest: Mice'), ('Pest: Rats', 'Pest: Rats'), ('Pest: Racoons', 'Pest: Racoons'), ('Pest: Squirrels', 'Pest: Squirrels'), ('Pest: Skunks', 'Pest: Skunks'), ('Pest: Opossums', 'Pest: Opossums'), ('Pest: Snakes', 'Pest: Snakes'), ('Pest: Bats', 'Pest: Bats'), ('Pest: Birds', 'Pest: Birds'), ('Construction', 'Construction'), ('Roofing Repair', 'Roofing Repair'), ('Insulation Install', 'Insulation Install'), ('Sheet Rock', 'Sheet Rock'), ('Cement Small Jobs', 'Cement Small Jobs')], max_length=50, null=True)),
                ('warranty_start_date', models.DateField(blank=True, null=True)),
                ('warranty_end_date', models.DateField(blank=True, null=True)),
                ('warranty', models.FileField(blank=True, default='', null=True, upload_to='')),
                ('invoice', models.FileField(blank=True, default='', null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('email', 'first_name', 'last_name', 'phone_number', 'service_address', 'warranty_end_date'),
            },
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='')),
                ('time', models.TimeField(default='')),
                ('comment', models.CharField(default='No Comments', max_length=250, null=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Working', 'Working'), ('Pending', 'Pending'), ('Complete', 'Complete')], default='Open', max_length=10)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
