from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Index'),
    path('Services', views.service, name="Services"),
    path('Consultations', views.consultation, name="Consultations"),
    path('FAQ', views.faq, name="FAQ"),
    path('Reviews', views.reviews, name="Reviews"),
    path('EditSuccess', views.edit_success, name="EditSuccess"),
    path('success', views.success, name="Success"),
    path('profile', views.profile, name="Profile"),
    path('edit_profile', views.edit_profile, name="EditProfile"),
]