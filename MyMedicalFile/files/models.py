from django.db import models

# Create your models here.


class Patient_File(models.Model):
    name = models.CharField(max_length=310)
    national_identity = models.IntegerField()
    blood_type = models.CharField(max_length=5)
    patient_history = models.TextField()
    def  __str__(self):
        return self.name
    class Meta:
        ordering = ['name']


class Doctor_File(models.Model):
    name = models.CharField(max_length=310)
    job_id = models.IntegerField()
    phone_number = models.IntegerField()
    address = models.TextField()
    def  __str__(self):
        return self.name

