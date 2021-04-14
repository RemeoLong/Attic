from django.urls import include, path
from . import views
from .views import *

app_name = Profile
urlpatterns = [

    path('EditSuccess', views.edit_success, name="EditSuccess"),
    path('<int:id>', views.profile, name="Profile"),
    path('<int:id>/edit_profile', ProfileUpdateView.as_view(), name="EditProfile"),

]