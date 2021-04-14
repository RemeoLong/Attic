from django.contrib import admin
from .models import Consultation


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'service_address')


admin.site.register(Consultation, ConsultationAdmin)
