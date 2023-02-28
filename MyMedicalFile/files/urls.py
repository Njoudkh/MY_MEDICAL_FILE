from django.urls import path
from . import views

urlpatterns = [
    path('file',views.file,name='file_page'),
    path('',views.files,name='files_page'),
]
