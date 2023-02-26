from django.urls import path
from . import views

urlpatterns = [
    path('file',views.file,name='file'),
    path('',views.files,name='files'),
]
