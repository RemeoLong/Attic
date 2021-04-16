from datetime import date

from django.db import models
from Attic.models import Consultation
from Profile.models import Profile


class Appointment(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, default='')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    consult_date = models.DateField(default='')
    consult_time = models.TimeField(default='')

    def __str__(self):
        return self.Appointment

    @property
    def consultation_filtering(self):
        return Appointment.objects.all().filter(Appointment_id=self.id)

    def todays_appointment(self):
        today = date.today()
        return Appointment.objects.filter(post_date__date=date.today())



