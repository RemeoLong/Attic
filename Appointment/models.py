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


class FirstFollowUp(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    date = models.DateField(default='')
    time = models.TimeField(default='')
    comment = models.CharField(max_length= 150, default='')

    def __str__(self):
        return self.profile


class SecondFollowUp(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    date = models.DateField(default='')
    time = models.TimeField(default='')
    comment = models.CharField(max_length= 150, default='')

    def __str__(self):
        return self.profile


class ThirdFollowUp(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    date = models.DateField(default='')
    time = models.TimeField(default='')
    comment = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.profile


class FourthFollowUp(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    date = models.DateField(default='')
    time = models.TimeField(default='')
    comment = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.profile


class FifthFollowUp(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    date = models.DateField(default='')
    time = models.TimeField(default='')
    comment = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.profile


class SixthFollowUp(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    date = models.DateField(default='')
    time = models.TimeField(default='')
    comment = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.profile
