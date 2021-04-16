from django.urls import include, path
from . import views
from .views import *

app_name = "Profile"
urlpatterns = [
    path('home', views.profile_home, name="Profile"),
    path('EditSuccess/', views.edit_success, name="EditSuccess"),
    path('edit_profile/<int:id>/', login_required(ProfileUpdateView.as_view()), name="EditProfile"),
    path('FollowUp', FollowUpCreateView.as_view(), name="FollowUp"),
]