from django.urls import path
from . import views

app_name = "main"

urlpatterns = [ 
 path("", views.index, name="index_page"),
 path("about", views.about, name="about_page"),
]