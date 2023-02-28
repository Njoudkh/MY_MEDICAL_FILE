from django.urls import path
from . import views


app_name='accounts'

urlpatterns = [
    path('login',views.login , name='login_page'),
    path('signup',views.signup , name='signup_page'),
    path('profile',views.profile , name='profile'),
    path('profile/edit',views.profile_edit , name='profile_edit'),
]
