from django.contrib import admin
from .models import Patient_File
from .models import Doctor_File
# Register your models here.

admin.site.register(Patient_File)
admin.site.register(Doctor_File)

