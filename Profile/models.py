from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.urls import reverse


class Profile(models.Model):
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=10, unique=True, default='')
    email = models.EmailField(max_length=200, unique=True)
    first_name = models.CharField(max_length=50, editable=True)
    last_name = models.CharField(max_length=50, editable=True)
    service_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15, editable=True)
    services = models.CharField(max_length=50, default='', editable=True, choices=service_choices)
    additional_service = models.CharField(max_length=50, null=True, blank=True, editable=True, choices=service_choices)
    warranty_start_date = models.DateField(null=True, blank=True, default='')
    warranty_end_date = models.DateField(null=True, blank=True, default='')
    warranty = models.FileField(null=True, blank=True, default='')
    invoice = models.FileField(null=True, blank=True, default='')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

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

    def get_absolute_url(self):
        return reverse('Profile:profile-detail', kwargs={'id': self.id})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)