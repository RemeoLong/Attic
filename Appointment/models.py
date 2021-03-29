from django.contrib.auth.models import User
from django.db import models
from Attic.models import Profile


class Appointment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    consult_date = models.DateTimeField(default='')
    first_check = models.DateTimeField(default='')
    second_check = models.DateTimeField(default='')
    third_check = models.DateTimeField(default='')
    fourth_check = models.DateTimeField(default='')
    fifth_check = models.DateTimeField(default='')

    def __str__(self):
        return self.Appointment

    @property
    def appointment_filtering(self):
        return Appointment.objects.all().filter(Appointment_id=self.id)

