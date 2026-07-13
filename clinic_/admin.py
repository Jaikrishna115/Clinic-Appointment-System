from django.contrib import admin
from .models import PatientProfile, DoctorProfile, Appointment

admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(Appointment)

# Register your models here.
