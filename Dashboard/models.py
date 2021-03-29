from django.db import models
from Attic.models import Consultation, Profile
from Appointment.models import Appointment


class Consultation(models.Model):
    consult_date = models.ForeignKey(Consultation, on_delete=models.CASCADE, default='')


class Profile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')


class Appointment(models.Model):
    consult_date = models.ForeignKey(Appointment, on_delete=models.CASCADE, default='')