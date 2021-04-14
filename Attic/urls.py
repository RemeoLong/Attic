from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='Index'),
    path('Services', views.service, name="Services"),
    path('Consultations', views.consultation, name="Consultations"),
    path('FAQ', views.faq, name="FAQ"),
    path('Reviews', views.reviews, name="Reviews"),
    path('EditSuccess', views.edit_success, name="EditSuccess"),
    path('success', views.success, name="Success"),
    path('profile', views.profile, name="Profile"),
    path('<slug:slug>', ProfileUpdateView.as_view(), name="EditProfile"),
]