from django.contrib import admin
from .models import Patient, Appointment, DischargeDetails

# Register your models here.
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(DischargeDetails)
