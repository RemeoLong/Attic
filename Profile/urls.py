from django.urls import include, path
from . import views
from .views import *

app_name = "Profile"
urlpatterns = [
    path('home', ProfileDetailView.as_view(), name="Profile"),
    path('edit_profile/<int:id>/', login_required(ProfileUpdateView.as_view()), name="EditProfile"),


    path('Appointment', FollowUpListView.as_view(), name="Appointment"),
    path('FollowUp', FollowUpCreateView.as_view(), name="CreateFollowUp"),
    path('EditFollowUp', FollowUpUpdateView.as_view(), name="EditFollowUp"),
    path('DeleteFollowUp', FollowUpDeleteView.as_view(), name="DeleteFollowUp"),

    path('EditSuccess/', views.edit_success, name="EditSuccess"),
]