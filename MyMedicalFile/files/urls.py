from django.urls import path
from . import views
app_name = "files"
urlpatterns = [
    path('file',views.file,name='file_page'),
    path('',views.files,name='files_page'),
]
