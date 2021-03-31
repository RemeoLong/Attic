from django.conf import settings
from django.db import models
from django.dispatch import receiver


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
    zip_code = models.CharField(max_length=10, editable=True)
    phone_number = models.CharField(max_length=15, editable=True)
    service = models.CharField(max_length=100, choices=service_choices)
    comment = models.TextField(default='')
    customer = models.BooleanField(default=False)

    def __str__(self):
        return self.Consultations

    @property
    def consult_filtering(self):
        return Consultation.objects.all().filter(Consltation_id=self.id)

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
        return self.consult_date

    def __str__(self):
        return self.consult_time

    #@receiver(post_save, sender=Consultation
    #def create_profile(sender, instance, **kwargs):
    #    if created:
    #        Profile.objects.create(user=instance)

    #@receiver(post_save, sender=Consultation)
    #def save_profile(sender, instance, **kwargs):
    #    instance.profile.save()


class Profile(models.Model):
    customer = models.ForeignKey(Consultation, on_delete=models.CASCADE, default='')
    email = models.EmailField(max_length=200, unique=True)
    first_name = models.CharField(max_length=50, editable=True)
    last_name = models.CharField(max_length=50, editable=True)
    service_address = models.CharField(max_length=100, editable=True)
    city = models.CharField(max_length=50, editable=True)
    state = models.CharField(max_length=2, editable=True)
    zip_code = models.CharField(max_length=10, editable=True)
    phone_number = models.CharField(max_length=15, editable=True)
    services = models.CharField(max_length=50, editable=True)
    warranty_start_date = models.DateField(default='')
    warranty_end_date = models.DateField(default='')

    def __str__(self):
        return self.Profile

    @property
    def profile_filtering(self):
        return Profile.objects.all().filter(Profile_id=self.id)

    class Meta:
        ordering = ('email', 'first_name', 'last_name', 'phone_number', 'service_address', 'warranty_end_date')

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
        return self.warranty_end_date
