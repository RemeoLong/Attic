from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'first_name', 'last_name', 'phone_number', 'service_address')


admin.site.register(Profile, ProfileAdmin)
