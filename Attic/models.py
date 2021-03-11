from django.conf import settings
from django.db import models


class Profile(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    first_name = models.CharField(max_length=50, editable=True)
    last_name = models.CharField(max_length=50, editable=True)
    service_address = models.CharField(max_length=100, editable=True)
    city = models.CharField(max_length=50, editable=True)
    state = models.CharField(max_length=2, editable=True)
    zip_code = models.IntegerField(editable=True)
    phone_number = models.IntegerField(editable=True)
    consult_date = models.DateField()
    warranty_date = models.DateField()


class Consultation(models.Model):
    service_choices = (
        ("Pest: Mice", "Pest: Mice"),
        ("Pest: Rats", "Pest: Rats"),
        ("Pest: Racoons", "Pest: Racoons"),
        ("Pest: Squirrels", "Pest: Squirrels"),
        ("Pest: Skunks", "Pest: Skunks"),
        ("Pest: Opossums", "Pest: Opossums"),
        ("Pest: Snakes", "Pest: Snakes"),
        ("Pest: Bats", "Pest: Bats"),
        ("Pest: Birds", "Pest: Birds"),
        ("Construction", "Construction"),
        ("Roofing Repair", "Roofing Repair"),
        ("Insulation Install", "Insulation Install"),
        ("Sheet Rock", "Sheet Rock"),
        ("Cement Small Jobs", "Cement Small Jobs"),
    )
    email = models.EmailField(max_length=200, unique=True)
    first_name = models.CharField(max_length=50, editable=True)
    last_name = models.CharField(max_length=50, editable=True)
    service_address = models.CharField(max_length=100, editable=True)
    city = models.CharField(max_length=50, editable=True)
    state = models.CharField(max_length=20, editable=True)
    zip_code = models.IntegerField(editable=True)
    phone_number = models.IntegerField(editable=True)
    service = models.CharField(max_length=100, choices=service_choices)
    comment = models.TextField(default='')





