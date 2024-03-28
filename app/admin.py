from django.contrib import admin

# Register your models here.
from .models import Patient_data, doctors_data

admin.site.register(Patient_data)
# admin.site.register(mri_patient_data)
admin.site.register(doctors_data)