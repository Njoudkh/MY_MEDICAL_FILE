from django.shortcuts import render
from .models import Patient_File

# Create your views here.

def file(request):
    return render (request, 'files/file.html')

def files(request):
    return render (request, 'files/files.html', {'fi':Patient_File.objects.all()})

