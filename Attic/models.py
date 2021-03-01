from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    first_name = models.CharField(max_length=50, editable=True)
    last_name = models.CharField(max_length=50, editable=True)
    service_address = models.CharField(max_length=100, editable=True)
    city = models.CharField(max_length=50, editable=True)
    state = models.CharField(max_length=2, editable=True)
    zip_code = models.IntegerField(editable=True)
    phone_number = models.IntegerField(editable=True)


class Consulation(models.Model):
    email = models.OneToOneField(Profile, on_delete=models.CASCADE)
    service_date = models.DateField(default='')
    service_time = models.TimeField(default='')





