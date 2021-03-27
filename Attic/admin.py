from django.contrib import admin
from .models import Profile, Consultation


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'service_address')


admin.site.register(Profile)
admin.site.register(Consultation, ConsultationAdmin)
