from django.contrib.auth.models import User
from django.db import models
from Attic.models import Profile, Consultation


class Consult(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, default='')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    consult_date = models.DateField(default='')
    consult_time = models.TimeField(default='')

    def __str__(self):
        return self.Appointment

    @property
    def appointment_filtering(self):
        return Consult.objects.all().filter(Appointment_id=self.id)


class FollowUp(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    first_check = models.DateTimeField(default='')
    second_check = models.DateTimeField(default='')
    third_check = models.DateTimeField(default='')
    fourth_check = models.DateTimeField(default='')
    fifth_check = models.DateTimeField(default='')

    def __str__(self):
        return self.profile
