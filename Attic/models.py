from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.urls import reverse


class Consultation(models.Model):
    status_choices = (
        ("New", "New"),
        ("Working", "Working"),
        ("Pending Customer", "Pending Customer"),
        ("Customer", "Customer")
    )
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
        ("Pest: Insects", "Pest: Insects"),
        ("Insulation Install", "Insulation Install"),
        ("Roofing Repair", "Roofing Repair"),
        ("Construction", "Construction"),
        ("Sheet Rock", "Sheet Rock"),
        ("Cement Small Jobs", "Cement Small Jobs"),
    )
    email = models.EmailField(max_length=200, unique=True)
    first_name = models.CharField(max_length=50, editable=True)
    last_name = models.CharField(max_length=50, editable=True)
    service_address = models.CharField(max_length=100, editable=True)
    city = models.CharField(max_length=50, editable=True)
    state = models.CharField(max_length=20, editable=True)
    zip_code = models.CharField(max_length=10, editable=True)
    phone_number = models.CharField(max_length=15, editable=True)
    service = models.CharField(max_length=100, choices=service_choices)
    consult_date = models.DateField(default='')
    consult_time = models.TimeField(default='')
    comment = models.TextField(default='No Comments')
    status = models.CharField(max_length=20, choices=status_choices, default="New")

    def __str__(self):
        return self.Consultation

    @property
    def consult_filtering(self):
        return Consultation.objects.all().filter(Consltation_id=self.id)

    @property
    def total(self):
        return Consultation.objects.count()

    @property
    def today_consult(self):
        return Consultation.objects.all().filter(date=datetime.today().date)

    class Meta:
        ordering = ('email', 'first_name', 'last_name', 'phone_number', 'service_address')

    def __str__(self):
        return self.email

    def __str__(self):
        return self.first_name

    def __str__(self):
        return self.last_name

    def __str__(self):
        return self.phone_number

    def __str__(self):
        return self.service_address

    def __str__(self):
        return str(self.consult_date)

    def __str__(self):
        return str(self.consult_time)

    #@receiver(post_save, sender=User)
    #def create_profile(sender, instance, **kwargs):
    #    if created:
    #        Profile.objects.create(user=instance)

    #@receiver(post_save, sender=User)
    #def save_profile(sender, instance, **kwargs):
    #    instance.profile.save()




