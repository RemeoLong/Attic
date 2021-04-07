from datetime import date

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
    def consultation_filtering(self):
        return Consult.objects.all().filter(Appointment_id=self.id)

    def todays_appointment(self):
        today = date.today()
        return Consult.objects.filter(post_date__date=date.today())


class FirstFollowUp(models.Model):
    status_choices = (
        ("Open", "Open"),
        ("Working", "Working"),
        ("Pending", "Pending"),
        ("Complete", "Complete"),
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    date = models.DateField(default='')
    time = models.TimeField(default='')
    comment = models.CharField(max_length=150, default='')
    status = models.CharField(max_length=10, choices=status_choices)

    def __str__(self):
        return self.profile


class SecondFollowUp(models.Model):
    status_choices = (
        ("Open", "Open"),
        ("Working", "Working"),
        ("Pending", "Pending"),
        ("Complete", "Complete"),
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    date = models.DateField(default='')
    time = models.TimeField(default='')
    comment = models.CharField(max_length=150, default='')
    status = models.CharField(max_length=10, choices=status_choices)

    def __str__(self):
        return self.profile


class ThirdFollowUp(models.Model):
    status_choices = (
        ("Open", "Open"),
        ("Working", "Working"),
        ("Pending", "Pending"),
        ("Complete", "Complete"),
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    date = models.DateField(default='')
    time = models.TimeField(default='')
    comment = models.CharField(max_length=150, default='')
    status = models.CharField(max_length=10, choices=status_choices)

    def __str__(self):
        return self.profile


class FourthFollowUp(models.Model):
    status_choices = (
        ("Open", "Open"),
        ("Working", "Working"),
        ("Pending", "Pending"),
        ("Complete", "Complete"),
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    date = models.DateField(default='')
    time = models.TimeField(default='')
    comment = models.CharField(max_length=150, default='')
    status = models.CharField(max_length=10, choices=status_choices)

    def __str__(self):
        return self.profile


class FifthFollowUp(models.Model):
    status_choices = (
        ("Open", "Open"),
        ("Working", "Working"),
        ("Pending", "Pending"),
        ("Complete", "Complete"),
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    date = models.DateField(default='')
    time = models.TimeField(default='')
    comment = models.CharField(max_length=150, default='')
    status = models.CharField(max_length=10, choices=status_choices)

    def __str__(self):
        return self.profile


class SixthFollowUp(models.Model):
    status_choices = (
        ("Open", "Open"),
        ("Working", "Working"),
        ("Pending", "Pending"),
        ("Complete", "Complete"),
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    date = models.DateField(default='')
    time = models.TimeField(default='')
    comment = models.CharField(max_length=150, default='')
    status = models.CharField(max_length=10, choices=status_choices)

    def __str__(self):
        return self.profile
