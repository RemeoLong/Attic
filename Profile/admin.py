from django.contrib import admin
from .models import Profile, FollowUp


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'first_name', 'last_name', 'phone_number', 'service_address')


class FollowUpAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'comment', 'status')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(FollowUp, FollowUpAdmin)
