from django.urls import path
from . import views

app_name = "main"

urlpatterns = [ 
 path("", views.index, name="index_page"),
 path("about_us", views.about_us, name="about_me_page"),
]